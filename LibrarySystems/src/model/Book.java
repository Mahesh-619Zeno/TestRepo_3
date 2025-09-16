package LibrarySystems.src.model;

public class Book {
    private int id;
    private String title;
    private String author;
    private boolean isAvailable;

    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isAvailable = true;
    }

    public int getId() { return id; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public boolean isAvailable() { return isAvailable; }

    public void borrow() { if (!this.isAvailable) { throw new IllegalStateException("Book is already borrowed."); } this.isAvailable = false; }
    public void returnBook() { if (this.isAvailable) { throw new IllegalStateException("Book was not borrowed."); } this.isAvailable = true; }

    @Override
    public String toString() {
        return id + " | " + title + " | " + author + " | Available: " + isAvailable;
    }
}
