package com.example.smartscan;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.firebase.ui.firestore.FirestoreRecyclerAdapter;
import com.firebase.ui.firestore.FirestoreRecyclerOptions;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;

public class ProductListAdapter extends FirestoreRecyclerAdapter<Product, ProductListAdapter.ProductViewHolder>{

    private Context context;
    private FirestoreRecyclerOptions options;

    /**
     * Create a new RecyclerView adapter that listens to a Firestore Query.  See {@link
     * FirestoreRecyclerOptions} for configuration options.
     *
     * @param options
     */
    public ProductListAdapter(@NonNull FirestoreRecyclerOptions<Product> options) {
        super(options);
        this.options = options;
    }

    @Override
    public int getItemCount() {
        return options.getSnapshots().size();
    }

    @Override
    protected void onBindViewHolder(@NotNull ProductViewHolder holder, int position, @NotNull Product p) {
        holder.ptext.setText(p.getBarcode());
        context = holder.pimage.getContext();

        new DownloadImageTask((ImageView) holder.pimage)
                .execute("https://img.rami-levy.co.il/product/" + p.getBarcode() + "/medium.jpg");


    }

    @NotNull
    @Override
    public ProductViewHolder onCreateViewHolder(@NotNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.product_list_row,parent,false);
        return new ProductViewHolder(view);
    }

    public class ProductViewHolder extends RecyclerView.ViewHolder {
        TextView ptext;
        ImageView pimage;
        ImageView pdelete;

        public ProductViewHolder( @NotNull View itemView) {
            super(itemView);
            ptext =itemView.findViewById(R.id.product_name_text);
            pimage = itemView.findViewById(R.id.product_image);
            pdelete = itemView.findViewById(R.id.icon_delete_product);
        }
    }

    private class DownloadImageTask extends AsyncTask<String, Void, Bitmap> {
        ImageView bmImage;

        public DownloadImageTask(ImageView bmImage) {
            this.bmImage = bmImage;
        }

        protected Bitmap doInBackground(String... urls) {
            String urldisplay = urls[0];
            Bitmap mIcon11 = null;
            try {
                InputStream in = new java.net.URL(urldisplay).openStream();
                mIcon11 = BitmapFactory.decodeStream(in);
            } catch (Exception e) {
                Log.e("Error", e.getMessage());
                e.printStackTrace();
            }
            return mIcon11;
        }

        protected void onPostExecute(Bitmap result) {
            bmImage.setImageBitmap(result);
        }
    }
}
