package com.example.smartscan;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Paint;
import android.graphics.drawable.Drawable;
import android.os.AsyncTask;
import android.util.Log;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.firebase.ui.firestore.FirestoreRecyclerAdapter;
import com.firebase.ui.firestore.FirestoreRecyclerOptions;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;

import org.jetbrains.annotations.NotNull;

import java.io.InputStream;
import java.util.Objects;

public class ArchivedListAdapter extends FirestoreRecyclerAdapter<Product, ArchivedListAdapter.ProductViewHolder>{

    private Context context;
    private FirestoreRecyclerOptions options;
    private FirebaseFirestore db;
    private String image_url;

    /**
     * Create a new RecyclerView adapter that listens to a Firestore Query.  See {@link
     * FirestoreRecyclerOptions} for configuration options.
     *
     * @param options
     */
    public ArchivedListAdapter(@NonNull FirestoreRecyclerOptions<Product> options) {
        super(options);
        this.options = options;
    }


    @Override
    public int getItemCount() {
        return options.getSnapshots().size();
    }

    @Override
    protected void onBindViewHolder(@NotNull ProductViewHolder holder, int position, @NotNull Product p) {
        db = FirebaseFirestore.getInstance();
        holder.ptext.setPaintFlags(holder.ptext.getPaintFlags() | Paint.STRIKE_THRU_TEXT_FLAG);
        holder.ptext.setText("");
        holder.ptext.setEnabled(false);
        Drawable originalDrawable = holder.ptext.getBackground();

        holder.ptext.setBackgroundResource(android.R.color.transparent);

        holder.pimage.setImageResource(R.drawable.ic_baseline_fastfood_24);

        if(p.getIs_identified() != null && p.getIs_identified() == false){
            holder.ptext.setText("לא ידוע");
            holder.ptext.setEnabled(false);
            holder.ptext.setSingleLine();
            holder.ptext.setBackground(originalDrawable);
            holder.ptext.setOnEditorActionListener(new TextView.OnEditorActionListener() {
                @Override
                public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                    if (actionId == 6) {
                        InputMethodManager imm = (InputMethodManager)v.getContext().getSystemService(Context.INPUT_METHOD_SERVICE);
                        imm.hideSoftInputFromWindow(v.getWindowToken(), 0);
                        holder.ptext.clearFocus();
                        p.setName(holder.ptext.getText().toString());
                        Toast.makeText(v.getContext(), holder.ptext.getText(), Toast.LENGTH_SHORT).show();
                    }
                    return true;
                }
            });
        }

        if(p.getProduct() != null){
            p.getProduct().get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                @Override
                public void onComplete(@NonNull @NotNull Task<DocumentSnapshot> task) {
                    if(task.getResult() != null){
                        if(task.getResult().get("name") != null) {
                            String name = Objects.requireNonNull(task.getResult().get("name")).toString();
                            p.setName(name);
                            holder.ptext.setText(name);
                        }
                        if(task.getResult().get("image") != null){
                            image_url = task.getResult().get("image").toString();
                            new DownloadImageTask((ImageView) holder.pimage)
                                    .execute(image_url);
                        }
                    }
                }
            });
        }

    }

    @NotNull
    @Override
    public ProductViewHolder onCreateViewHolder(@NotNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.archive_list_row,parent,false);
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
