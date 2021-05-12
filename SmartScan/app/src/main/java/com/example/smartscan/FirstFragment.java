package com.example.smartscan;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiManager;
import android.os.Build;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import com.example.smartscan.databinding.FragmentFirstBinding;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.GoogleAuthCredential;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;

import java.util.List;

public class FirstFragment extends Fragment {

    private FragmentFirstBinding binding;
    private EditText wifi_ssid;
    private EditText wifi_password;
    private ImageView barcode;


    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {

        binding = FragmentFirstBinding.inflate(inflater, container, false);
        return binding.getRoot();

    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        wifi_ssid = binding.wifiSsid;
        wifi_password = binding.wifiPassword;
        barcode = binding.barcodeImage;


        binding.generateBarcode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                barCodeButton();
            }
        });
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }

    public void barCodeButton(){
        MultiFormatWriter multiFormatWriter= new MultiFormatWriter();
        try {
            BitMatrix bitMatrix = multiFormatWriter.encode(wifi_ssid.getText().toString() +
                    ";" + wifi_password.getText().toString(), BarcodeFormat.CODE_128,
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
}