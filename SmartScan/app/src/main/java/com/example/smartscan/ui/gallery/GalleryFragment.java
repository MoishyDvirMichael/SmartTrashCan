package com.example.smartscan.ui.gallery;

import android.Manifest;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.Gravity;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.smartscan.FirstFragment;
import com.example.smartscan.R;
import com.example.smartscan.databinding.FragmentFirstBinding;
import com.example.smartscan.databinding.FragmentGalleryBinding;
import com.google.firebase.auth.FirebaseAuth;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class GalleryFragment extends Fragment {

    private FragmentGalleryBinding binding;
    private Spinner wifi_ssid;
    private EditText wifi_password;
    private ImageView barcode;
    private WifiManager wifiManager;
    private WifiReceiver wifiReceiver;
    private FirebaseAuth acct;




    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {

        binding = FragmentGalleryBinding.inflate(inflater, container, false);
        return binding.getRoot();

    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        wifi_ssid = binding.wifiSsid;
        wifi_password = binding.wifiPassword;
        barcode = binding.barcodeImage;
        wifiManager = (WifiManager) getActivity().getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        wifiReceiver = new WifiReceiver();

        getActivity().getApplicationContext().registerReceiver(wifiReceiver,
                new IntentFilter(wifiManager.SCAN_RESULTS_AVAILABLE_ACTION));

        if(ContextCompat.checkSelfPermission(getActivity().getApplicationContext(),
                Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(getActivity(),new String[]{Manifest.permission.ACCESS_FINE_LOCATION},0);
        }

        acct = FirebaseAuth.getInstance();
        scanWifi();
        binding.generateBarcode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    barCodeButton();
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                binding.firstFragmentNext.setVisibility(View.VISIBLE);
            }
        });
        wifi_password.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });
        binding.firstFragmentNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                    NavHostFragment.findNavController(GalleryFragment.this)
                            .navigate(R.id.action_GalleryFragment_to_HomeFragment);
            }
        });
        binding.firstFragmentNext.setVisibility(View.INVISIBLE);
    }

    @Override
    public void onStart() {
        super.onStart();

        wifi_ssid.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                if(parent.getChildAt(0) != null){
                    ((TextView) parent.getChildAt(0)).setTextColor(Color.BLACK);
                    ((TextView) parent.getChildAt(0)).setTextSize(24);
                    ((TextView) parent.getChildAt(0)).setGravity(Gravity.CENTER);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
    }

    @Override
    public void onResume() {
        super.onResume();
        wifi_ssid.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                if(parent.getChildAt(0) != null){
                    ((TextView) parent.getChildAt(0)).setTextColor(Color.BLACK);
                    ((TextView) parent.getChildAt(0)).setTextSize(16);
                    ((TextView) parent.getChildAt(0)).setGravity(Gravity.CENTER);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
    }

    private void scanWifi() {
        wifiManager.startScan();
        List<ScanResult> results = wifiManager.getScanResults();
        ArrayList<String> wifi_names = new ArrayList<>();
        for(ScanResult wifi : results){
            wifi_names.add(wifi.SSID);
        }
        ArrayAdapter<String> wifiAdapter = new ArrayAdapter<String>(getActivity(), android.R.layout.simple_spinner_item, wifi_names);
        wifiAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        wifi_ssid.setAdapter(wifiAdapter);
        wifiAdapter.notifyDataSetChanged();
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }

    public void barCodeButton() throws JSONException {
        binding.generateBarcode.setText(R.string.regenerate);
        JSONObject qr_json = new JSONObject();
        qr_json.put("uid", acct.getUid());
        qr_json.put("wifi_name", wifi_ssid.getSelectedItem().toString());
        qr_json.put("wifi_password", wifi_password.getText().toString());
        String qr_string = qr_json.toString();
        MultiFormatWriter multiFormatWriter= new MultiFormatWriter();
        try {
            BitMatrix bitMatrix = multiFormatWriter.encode(qr_string, BarcodeFormat.QR_CODE,
                    barcode.getWidth(),barcode.getHeight());
            Bitmap bitmap = Bitmap.createBitmap(barcode.getWidth(), barcode.getHeight(), Bitmap.Config.RGB_565);
            for(int i = 0; i < barcode.getWidth(); i++){
                for(int j = 0; j< barcode.getHeight(); j++){
                    bitmap.setPixel(i, j, bitMatrix.get(i,j)? Color.BLACK: Color.WHITE);
                }
            }
            barcode.setImageBitmap(bitmap);
        } catch (WriterException e) {
            e.printStackTrace();
        }

    }

    class WifiReceiver extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {

        }
    }


    void checkFieldsForEmptyValues(){
        Button b = (Button) binding.generateBarcode;

        String s1 = wifi_password.getText().toString();

        if(s1.equals("")){
            b.setEnabled(false);
        } else {
            b.setEnabled(true);
        }
    }



}