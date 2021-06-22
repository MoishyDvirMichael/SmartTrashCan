package com.example.smartscan.ui.home;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.ItemTouchHelper;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.smartscan.ArchivedListAdapter;
import com.example.smartscan.Product;
import com.example.smartscan.ProductListAdapter;
import com.example.smartscan.R;
import com.example.smartscan.ui.Helper.MySwipeHelper;
import com.firebase.ui.common.ChangeEventType;
import com.firebase.ui.firestore.ChangeEventListener;
import com.firebase.ui.firestore.FirestoreRecyclerOptions;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import org.jetbrains.annotations.NotNull;

import java.util.List;

import static com.firebase.ui.auth.ui.email.RegisterEmailFragment.TAG;

public class HomeFragment extends Fragment {
    private FirebaseAuth mAuth;
    private FirebaseFirestore db;
    private ProductListAdapter adapter;
    private RecyclerView recyclerView;
    private FirestoreRecyclerOptions<Product> options;

    private ArchivedListAdapter archive_adapter;
    private RecyclerView archive_list;
    private FirestoreRecyclerOptions<Product> archive_options;
    private String uuid;



    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        HomeViewModel homeViewModel = new ViewModelProvider(this).get(HomeViewModel.class);
        View root = inflater.inflate(R.layout.fragment_home, container, false);
        mAuth = FirebaseAuth.getInstance();
        db = FirebaseFirestore.getInstance();
        recyclerView = root.findViewById(R.id.recycler_list_products);
        archive_list = root.findViewById(R.id.recycler_list_archive);
        uuid = mAuth.getUid();

        setProductList();
        setArchiveList();

        final TextView textView = root.findViewById(R.id.text_home);
        homeViewModel.getText().observe(getViewLifecycleOwner(), new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                textView.setText(s);
            }
        });

        return root;
    }

    private void setArchiveList() {
        CollectionReference ref = db
                .collection("users")
                .document(uuid)
                .collection("archived_products");
        Query query = ref.orderBy("barcode", Query.Direction.DESCENDING);
        archive_options = new FirestoreRecyclerOptions.Builder<Product>()
                .setQuery(query, Product.class)
                .build();
        archive_options.getSnapshots().addChangeEventListener(new ChangeEventListener() {
            @Override
            public void onChildChanged(@NonNull @NotNull ChangeEventType type, @NonNull @NotNull DocumentSnapshot snapshot, int newIndex, int oldIndex) {
                archive_adapter.notifyDataSetChanged();
            }

            @Override
            public void onDataChanged() {
                archive_adapter.notifyDataSetChanged();
            }

            @Override
            public void onError(@NonNull @NotNull FirebaseFirestoreException e) {

            }
        });
        archive_adapter = new ArchivedListAdapter(archive_options);
        archive_list.setAdapter(archive_adapter);
        archive_list.setLayoutManager(new LinearLayoutManager(getActivity()));
        archive_list.setHasFixedSize(true);
        archive_adapter.notifyDataSetChanged();

        MySwipeHelper swipeHelper1 = addNewSwipeAction1(archive_list, archive_adapter, "Delete", 0, "#FF3C30");
        ItemTouchHelper itemTouchHelper1 = new ItemTouchHelper(swipeHelper1);
        itemTouchHelper1.attachToRecyclerView(archive_list);

    }


    private void setProductList() {
        CollectionReference ref = db
                .collection("users")
                .document(uuid)
                .collection("scanned_products");
        Query query = ref.orderBy("barcode", Query.Direction.DESCENDING);
        options = new FirestoreRecyclerOptions.Builder<Product>()
                .setQuery(query, Product.class)
                .build();
        options.getSnapshots().addChangeEventListener(new ChangeEventListener() {
            @Override
            public void onChildChanged(@NonNull @NotNull ChangeEventType type, @NonNull @NotNull DocumentSnapshot snapshot, int newIndex, int oldIndex) {
                adapter.notifyDataSetChanged();
            }

            @Override
            public void onDataChanged() {
                adapter.notifyDataSetChanged();
            }

            @Override
            public void onError(@NonNull @NotNull FirebaseFirestoreException e) {

            }
        });
        adapter = new ProductListAdapter(options);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
        recyclerView.setHasFixedSize(true);
        adapter.notifyDataSetChanged();
        MySwipeHelper swipeHelper = addNewSwipeAction(recyclerView, adapter,"Archive", 0, "#FF3C30");
        ItemTouchHelper itemTouchHelper = new ItemTouchHelper(swipeHelper);
        itemTouchHelper.attachToRecyclerView(recyclerView);
    }

    private MySwipeHelper addNewSwipeAction(RecyclerView recyclerview, ProductListAdapter adapter1, String action_text, int drawable_id, String color) {
        return new MySwipeHelper(getContext(), recyclerview) {
            @Override
            public void instantiateUnderlayButton(RecyclerView.ViewHolder viewHolder, List<UnderlayButton> underlayButtons) {
                underlayButtons.add(new MySwipeHelper.UnderlayButton(
                        action_text,
                        drawable_id,
                        Color.parseColor(color),
                        getContext(),
                        new MySwipeHelper.UnderlayButtonClickListener() {
                            @Override
                            public void onClick(int pos) {
                                Long barcode = adapter1.getItem(viewHolder.getAdapterPosition()).getBarcode();
                                final FirebaseFirestore db = FirebaseFirestore.getInstance();
                                db.collection("users")
                                        .document(mAuth.getUid())
                                        .collection("scanned_products")
                                        .whereEqualTo("barcode", barcode)
                                        .get()
                                        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                                            @Override
                                            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                                                if (task.isSuccessful()) {
                                                    for (QueryDocumentSnapshot document : task.getResult()) {
                                                        DocumentReference to_delete = document.getReference();
                                                        DocumentReference dest = db.collection("users")
                                                                .document(mAuth.getUid())
                                                                .collection("archived_products")
                                                                .document();
                                                        moveFirestoreDocument(to_delete, dest);
                                                        break;
                                                    }
                                                } else {
                                                    Log.d(TAG, "Error getting documents: ", task.getException());
                                                }
                                            }
                                        });
                            }
                        }
                ));

            }
        };
    }

    private MySwipeHelper addNewSwipeAction1(RecyclerView recyclerview, ArchivedListAdapter adapter1, String action_text, int drawable_id, String color) {
        return new MySwipeHelper(getContext(), recyclerview) {
            @Override
            public void instantiateUnderlayButton(RecyclerView.ViewHolder viewHolder, List<UnderlayButton> underlayButtons) {
                underlayButtons.add(new MySwipeHelper.UnderlayButton(
                        action_text,
                        drawable_id,
                        Color.parseColor(color),
                        getContext(),
                        new MySwipeHelper.UnderlayButtonClickListener() {
                            @Override
                            public void onClick(int pos) {
                                Long barcode = adapter1.getItem(viewHolder.getAdapterPosition()).getBarcode();
                                AlertDialog.Builder builder = new AlertDialog.Builder(getContext());
                                builder.setMessage("Are you sure you want to delete this product?")
                                        .setTitle("DELETE");
                                builder.setPositiveButton("YES", new DialogInterface.OnClickListener() {
                                    public void onClick(DialogInterface dialog, int id) {
                                        final FirebaseFirestore db = FirebaseFirestore.getInstance();
                                        db.collection("users")
                                                .document(mAuth.getUid())
                                                .collection("archived_products")
                                                .whereEqualTo("barcode", barcode)
                                                .get()
                                                .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                                                    @Override
                                                    public void onComplete(@NonNull Task<QuerySnapshot> task) {
                                                        if (task.isSuccessful()) {
                                                            for (QueryDocumentSnapshot document : task.getResult()) {
                                                                DocumentReference to_delete = document.getReference();
                                                                to_delete.delete().addOnSuccessListener(new OnSuccessListener<Void>() {
                                                                    @Override
                                                                    public void onSuccess(Void aVoid) {
                                                                        adapter1.notifyDataSetChanged();
                                                                    }
                                                                });
                                                                break;
                                                            }
                                                        } else {
                                                            Log.d(TAG, "Error getting documents: ", task.getException());
                                                        }
                                                    }
                                                });
                                    }
                                });
                                builder.setNegativeButton("NO", new DialogInterface.OnClickListener() {
                                    public void onClick(DialogInterface dialog, int id) {
                                        dialog.dismiss();
                                    }
                                });
                                AlertDialog dialog = builder.create();
                                dialog.show();
                            }
                        }
                ));
                underlayButtons.add(new MySwipeHelper.UnderlayButton(
                        "Restore",
                        drawable_id,
                        Color.parseColor("#3E9C00"),
                        getContext(),
                        new MySwipeHelper.UnderlayButtonClickListener() {
                            @Override
                            public void onClick(int pos) {
                                Long barcode = adapter1.getItem(viewHolder.getAdapterPosition()).getBarcode();
                                final FirebaseFirestore db = FirebaseFirestore.getInstance();
                                db.collection("users")
                                        .document(mAuth.getUid())
                                        .collection("archived_products")
                                        .whereEqualTo("barcode", barcode)
                                        .get()
                                        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                                            @Override
                                            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                                                if (task.isSuccessful()) {
                                                    for (QueryDocumentSnapshot document : task.getResult()) {
                                                        DocumentReference to_delete = document.getReference();
                                                        DocumentReference dest = db.collection("users")
                                                                .document(mAuth.getUid())
                                                                .collection("scanned_products")
                                                                .document();
                                                        moveFirestoreDocument(to_delete, dest);
                                                    }
                                                } else {
                                                    Log.d(TAG, "Error getting documents: ", task.getException());
                                                }
                                            }
                                        });
                            }
                        }
                ));
            }
        };
    }


    @Override
    public void onStart() {
        super.onStart();
        adapter.startListening();
    }

    @Override
    public void onStop() {
        super.onStop();
        adapter.stopListening();
    }

    public void moveFirestoreDocument(DocumentReference fromPath, final DocumentReference toPath) {
        fromPath.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
            @Override
            public void onComplete(@NonNull Task<DocumentSnapshot> task) {
                if (task.isSuccessful()) {
                    DocumentSnapshot document = task.getResult();
                    if (document != null) {
                        toPath.set(document.getData())
                                .addOnSuccessListener(new OnSuccessListener<Void>() {
                                    @Override
                                    public void onSuccess(Void aVoid) {
                                        Log.d(TAG, "DocumentSnapshot successfully written!");
                                        fromPath.delete()
                                                .addOnSuccessListener(new OnSuccessListener<Void>() {
                                                    @Override
                                                    public void onSuccess(Void aVoid) {
                                                        Log.d(TAG, "DocumentSnapshot successfully deleted!");
                                                    }
                                                })
                                                .addOnFailureListener(new OnFailureListener() {
                                                    @Override
                                                    public void onFailure(@NonNull Exception e) {
                                                        Log.w(TAG, "Error deleting document", e);
                                                    }
                                                });
                                    }
                                })
                                .addOnFailureListener(new OnFailureListener() {
                                    @Override
                                    public void onFailure(@NonNull Exception e) {
                                        Log.w(TAG, "Error writing document", e);
                                    }
                                });
                    } else {
                        Log.d(TAG, "No such document");
                    }
                } else {
                    Log.d(TAG, "get failed with ", task.getException());
                }
            }
        });
    }



}