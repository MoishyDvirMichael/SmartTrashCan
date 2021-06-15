package com.example.smartscan;

import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.Matrix;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import com.example.smartscan.databinding.FragmentSecondBinding;
import com.google.android.gms.auth.api.signin.GoogleSignIn;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.firebase.auth.FirebaseAuth;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;

public class SecondFragment extends Fragment {
    private ImageView barcode_log_in;
    private FirebaseAuth acct;

    private FragmentSecondBinding binding;

    @Override
    public void onCreate(@Nullable @org.jetbrains.annotations.Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

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
        acct = FirebaseAuth.getInstance();
        binding.buttonSecond.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getActivity().finish();

            }
        });

        barCodeButton();

    }




    public void barCodeButton(){
        final int width = 350;
        final int height = 150;
        MultiFormatWriter multiFormatWriter= new MultiFormatWriter();
        try {
            BitMatrix bitMatrix = multiFormatWriter.encode(acct.getUid(), BarcodeFormat.CODE_128,
                    width,height);
            Bitmap bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.RGB_565);
            for(int i = 0; i < width; i++){
                for(int j = 0; j< height; j++){
                    bitmap.setPixel(i, j, bitMatrix.get(i,j)? Color.BLACK: Color.WHITE);
                }
            }
            barcode_log_in.setImageBitmap(bitmap);
        } catch (WriterException e) {
            e.printStackTrace();
        }

    }

}