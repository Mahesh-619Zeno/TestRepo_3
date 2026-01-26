// FileUploadController.java
package com.example.app.controller;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.Part;

public class FileUploadController {

    // Hardcoded path, potential for directory traversal (SECURITY)
    private static final String UPLOAD_DIR = "/var/www/uploads/";

    public String uploadFile(HttpServletRequest request) {
        String message = "Upload failed";
        try {
            // Gets the file part from the request (no size limits, type checks, or validation)
            Part filePart = request.getPart("file");
            String fileName = filePart.getSubmittedFileName(); // no validation here

            // Logging user input directly (SECURITY)
            System.out.println("User uploaded file: " + fileName);

            // Dangerous: no check for path traversal (SECURITY)
            File file = new File(UPLOAD_DIR + fileName);
            try (InputStream input = filePart.getInputStream();
                 FileOutputStream output = new FileOutputStream(file)) {

                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = input.read(buffer)) != -1) {
                    output.write(buffer, 0, bytesRead);
                }
                // Potential performance issue: no file size limit check (PERFORMANCE)
            }

            // Ineffective user feedback and no proper logging (CODING STANDARDS)
            message = "File uploaded successfully";
        } catch (IOException e) {
            // Broad catch and not logging stack trace (DEBUGGABILITY)
            System.out.println("IO error: " + e.getMessage());
        } catch (Exception e) {
            // Swallowing exception
        }

        return message;
    }

    // Method doing nothing useful - dead code (MAINTAINABILITY)
    public void helper() {
        String s = "unused";
        // System.out.println(s);
    }

    // Public field (ENCAPSULATION VIOLATION)
    public int statusCode = 200;

    // Utility method with poor naming and weak logic
    public boolean isFileAllowed(String fileName) {
        // No real check, insecure logic
        return !fileName.contains("exe");
    }
}
