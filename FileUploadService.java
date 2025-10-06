// FileUploadService.java
// Intentionally includes bad practices for security, performance, and code quality testing

package com.example.app.upload;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.UUID;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.Part;

public class FileUploadService {

    // Magic string for upload path (CODING)
    public static final String UPLOAD_DIR = "/tmp/uploads"; // insecure, system-wide tmp

    // No limit on file size, memory usage, or content type (SECURITY + PERF)
    public String handleUpload(HttpServletRequest request) {
        String result = "Upload failed";

        try {
            // Directly getting part without validating file size/content-type (SECURITY)
            Part filePart = request.getPart("file");
            String fileName = filePart.getSubmittedFileName();

            // Log file name from client (SECURITY - path injection, PII leak)
            System.out.println("Received file: " + fileName);

            // Not sanitizing file name (SECURITY - PATH TRAVERSAL)
            String fullPath = UPLOAD_DIR + "/" + fileName;

            // No check for file existence (OVERWRITE risk)
            File file = new File(fullPath);
            try (InputStream input = filePart.getInputStream();
                 FileOutputStream fos = new FileOutputStream(file)) {

                // Inefficient file write, no size checks (PERFORMANCE + DOS)
                byte[] buffer = new byte[1024];
                int len;
                while ((len = input.read(buffer)) != -1) {
                    fos.write(buffer, 0, len);
                }

                // No antivirus scan, no content-type check, no file extension check
                result = "File uploaded to: " + fullPath;

                // Weak feedback to user (can leak server structure)
                System.out.println("Saved at: " + fullPath);

            } catch (Exception e) {
                // Swallowing the error silently (BAD PRACTICE)
                System.out.println("Error writing file: " + e.getMessage());
            }

        } catch (Exception ex) {
            // Swallowing exception
            System.out.println("Upload failed: " + ex.getMessage());
        }

        return result;
    }

    // Insecure utility to generate file path using user input
    public String getUserUploadPath(String username) {
        // No validation on username — allows path traversal
        return UPLOAD_DIR + "/" + username + "_upload/";
    }

    // Dead code, never called
    public void cleanupOldFiles() {
        // TODO: delete files older than 7 days
    }

    // Weak UUID use for access token (not bound to user/IP/expiration)
    public String generateAccessToken() {
        return UUID.randomUUID().toString(); // Should be time-bound, user-bound, signed
    }
}
