package com.example.smartscan;

import android.graphics.Bitmap;
import android.graphics.Color;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import com.example.smartscan.databinding.FragmentSecondBinding;
import com.google.android.gms.auth.api.signin.GoogleSignIn;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;

public class SecondFragment extends Fragment {
    private ImageView barcode_log_in;
    private GoogleSignInAccount acct;

    private FragmentSecondBinding binding;

    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {

        binding = FragmentSecondBinding.inflate(inflater, container, false);
        return binding.getRoot();

    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        barcode_log_in = binding.barcodeLogIn;
        acct = GoogleSignIn.getLastSignedInAccount(getActivity());

        binding.buttonSecond.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NavHostFragment.findNavController(SecondFragment.this)
                        .navigate(R.id.action_SecondFragment_to_FirstFragment);
            }
        });
    }



    public void barCodeButton(){
        MultiFormatWriter multiFormatWriter= new MultiFormatWriter();
        try {
            BitMatrix bitMatrix = multiFormatWriter.encode(acct.getId(), BarcodeFormat.CODE_128,
                    barcode_log_in.getWidth(),barcode_log_in.getHeight());
            Bitmap bitmap = Bitmap.createBitmap(barcode_log_in.getWidth(), barcode_log_in.getHeight(), Bitmap.Config.RGB_565);
            for(int i = 0; i < barcode_log_in.getWidth(); i++){
                for(int j = 0; j< barcode_log_in.getHeight(); j++){
                    bitmap.setPixel(i, j, bitMatrix.get(i,j)? Color.BLACK: Color.WHITE);
                }
            }
            barcode_log_in.setImageBitmap(bitmap);
        } catch (WriterException e) {
            e.printStackTrace();
        }

    }

}