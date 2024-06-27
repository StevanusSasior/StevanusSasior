
aplikasi GUI Swing

*Langkah-langkah Utama*:
1. *Membuat GUI*: Membuat form dengan Swing yang memiliki field untuk input data dan tombol untuk operasi database.
2. *Menghubungkan ke Database*: Menggunakan JDBC untuk menghubungkan ke database.
3. *Melakukan Operasi CRUD*: Menambahkan, menghapus, memperbarui, dan melihat data di tabel `tbl_barang`.

 Kode Program

```java
import javax.swing.;
import java.awt.;
import java.awt.event.;
import java.sql.*;

public class TokoBarangApp extends JFrame {
    // Database parameters
    private static final String DB_URL = "jdbc:mysql://localhost:3306/toko"; // URL database
    private static final String DB_USERNAME = "root"; // Username database
    private static final String DB_PASSWORD = "password"; // Password database

    // GUI components
    private JTextField idField, nameField, priceField, quantityField;
    private JButton addButton, updateButton, deleteButton, viewButton;
    private JTextArea resultArea;

    public TokoBarangApp() {
        // Set up the form
        setTitle("Toko Barang Management");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        
        // Initialize components
        idField = new JTextField(10);
        nameField = new JTextField(10);
        priceField = new JTextField(10);
        quantityField = new JTextField(10);
        addButton = new JButton("Add");
        updateButton = new JButton("Update");
        deleteButton = new JButton("Delete");
        viewButton = new JButton("View All");
        resultArea = new JTextArea(10, 30);
        resultArea.setEditable(false);

        // Layout setup
        JPanel panel = new JPanel(new GridLayout(6, 2));
        panel.add(new JLabel("ID:"));
        panel.add(idField);
        panel.add(new JLabel("Name:"));
        panel.add(nameField);
        panel.add(new JLabel("Price:"));
        panel.add(priceField);
        panel.add(new JLabel("Quantity:"));
        panel.add(quantityField);
        panel.add(addButton);
        panel.add(updateButton);
        panel.add(deleteButton);
        panel.add(viewButton);

        // Add components to frame
        add(panel, BorderLayout.NORTH);
        add(new JScrollPane(resultArea), BorderLayout.CENTER);

        // Add action listeners for buttons
        addButton.addActionListener(e -> addItem());
        updateButton.addActionListener(e -> updateItem());
        deleteButton.addActionListener(e -> deleteItem());
        viewButton.addActionListener(e -> viewItems());

        setVisible(true);
    }

    // Method to connect to the database
    private Connection connect() throws SQLException {
        return DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
    }

    // Method to add a new item
    private void addItem() {
        String id = idField.getText();
        String name = nameField.getText();
        String price = priceField.getText();
        String quantity = quantityField.getText();

        String query = "INSERT INTO tbl_barang (id, name, price, quantity) VALUES (?, ?, ?, ?)";

        try (Connection conn = connect(); PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, id);
            stmt.setString(2, name);
            stmt.setString(3, price);
            stmt.setString(4, quantity);
            stmt.executeUpdate();
            resultArea.setText("Item added successfully.");
        } catch (SQLException e) {
            resultArea.setText("Error adding item: " + e.getMessage());
        }
    }

    // Method to update an existing item
    private void updateItem() {
        String id = idField.getText();
        String name = nameField.getText();
        String price = priceField.getText();
        String quantity = quantityField.getText();

        String query = "UPDATE tbl_barang SET name = ?, price = ?, quantity = ? WHERE id = ?";

        try (Connection conn = connect(); PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, name);
            stmt.setString(2, price);
            stmt.setString(3, quantity);
            stmt.setString(4, id);
            stmt.executeUpdate();
            resultArea.setText("Item updated successfully.");
        } catch (SQLException e) {
            resultArea.setText("Error updating item: " + e.getMessage());
        }
    }

    // Method to delete an item
    private void deleteItem() {
        String id = idField.getText();

        String query = "DELETE FROM tbl_barang WHERE id = ?";

        try (Connection conn = connect(); PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, id);
            stmt.executeUpdate();
            resultArea.setText("Item deleted successfully.");
        } catch (SQLException e) {
            resultArea.setText("Error deleting item: " + e.getMessage());
        }
    }

    // Method to view all items
    private void viewItems() {
        String query = "SELECT * FROM tbl_barang";

        try (Connection conn = connect(); Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(query)) {
            StringBuilder sb = new StringBuilder();
            while (rs.next()) {
                sb.append("ID: ").append(rs.getString("id")).append(", ");
                sb.append("Name: ").append(rs.getString("name")).append(", ");
                sb.append("Price: ").append(rs.getString("price")).append(", ");
                sb.append("Quantity: ").append(rs.getString("quantity")).append("\n");
            }
            resultArea.setText(sb.toString());
        } catch (SQLException e) {
            resultArea.setText("Error fetching items: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TokoBarangApp::new);
    }
}
```

 Penjelasan:

1. *Parameter Koneksi Database*:
   - URL, nama pengguna (username), dan kata sandi (password) yang digunakan untuk menghubungkan ke database `toko`.
   
2. *Komponen GUI*:
   - Field teks (`JTextField`) untuk memasukkan ID, nama, harga, dan kuantitas barang.
   - Tombol (`JButton`) untuk melakukan operasi seperti tambah (`Add`), perbarui (`Update`), hapus (`Delete`), dan lihat (`View All`).
   - Area teks (`JTextArea`) untuk menampilkan hasil atau pesan dari operasi yang dilakukan.

3. *Metode Koneksi dan Operasi CRUD*:
   - *connect()*: Menghubungkan ke database menggunakan JDBC.
   - *addItem()*: Menambahkan item baru ke dalam tabel `tbl_barang`.
   - *updateItem()*: Memperbarui item yang ada di dalam tabel `tbl_barang`.
   - *deleteItem()*: Menghapus item dari tabel `tbl_barang`.
   - *viewItems()*: Melihat semua item di tabel `tbl_barang`.

# Cara Menjalankan Program:
1. Pastikan Anda memiliki server MySQL yang berjalan dengan database bernama `toko` dan tabel `tbl_barang` yang memiliki kolom `id`, `name`, `price`, dan `quantity`.
2. Perbarui parameter `DB_URL`, `DB_USERNAME`, dan `DB_PASSWORD` sesuai dengan konfigurasi database Anda.
3. Jalankan program sebagai aplikasi Java dari IDE atau terminal.

Dengan mengikuti langkah-langkah ini, Anda akan memiliki aplikasi GUI sederhana yang dapat memanipulasi data dalam tabel `tbl_barang` dari database `toko`.
