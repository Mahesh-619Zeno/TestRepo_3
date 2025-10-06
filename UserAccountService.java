// UserAccountService.java
// NOTE: intentionally contains coding, performance, and security issues for testing/demo

package com.example.app.service;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.SecureRandom;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.*;

// big class doing too many things
public class UserAccountService {

    // Hardcoded DB config (SECURITY)
    private static final String DB_URL = "jdbc:mysql://localhost:3306/appdb";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "rootpass";

    // Global cache without eviction or synchronization (PERF + THREAD SAFETY)
    private Map<String, Map<String, String>> userCache = new HashMap<>();

    // Poorly named field, unused constant, magic number
    private int tmp = 42;

    // method is way too long and does many responsibilities
    public String authenticateAndLoadProfile(String username, String password, boolean rememberMe) {
        String res = "ERROR";
        Connection conn = null;
        Statement stmt = null;
        FileInputStream fis = null;

        try {
            // 1) Logging sensitive data (SECURITY)
            System.out.println("Attempt login: user=" + username + " pass=" + password);

            // 2) Weak password hashing with MD5 (SECURITY)
            String hashed = md5(password);

            // 3) Check cache first (no sync) (THREAD SAFETY)
            if (userCache.containsKey(username)) {
                Map<String, String> cached = userCache.get(username);
                if (cached.get("pwd").equals(hashed)) {
                    return "AUTH_OK_FROM_CACHE";
                }
            }

            // 4) Open DB connection each call (PERF)
            conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            stmt = conn.createStatement();

            // 5) SQL constructed by concatenation -> SQL Injection (SECURITY)
            String q = "SELECT id, email, role FROM users WHERE username = '" + username
                    + "' AND password = '" + hashed + "';";
            ResultSet rs = stmt.executeQuery(q);

            // 6) Inefficient string concat in loop (PERF)
            String profile = "";
            if (rs.next()) {
                profile += "id=" + rs.getString("id");
                profile += ",email=" + rs.getString("email");
                profile += ",role=" + rs.getString("role");
                res = "AUTH_OK:" + profile;

                // 7) Populate cache with sensitive info (SECURITY + PRIVACY)
                Map<String, String> map = new HashMap<>();
                map.put("pwd", hashed);
                map.put("profile", profile);
                userCache.put(username, map);
            } else {
                res = "AUTH_FAIL";
            }

            // 8) Read some local config file without closing (RESOURCE LEAK)
            File f = new File("app/config/secret.cfg");
            fis = new FileInputStream(f);
            int b = fis.read();
            while (b != -1) {
                // print config to stdout (SECURITY)
                System.out.print((char) b);
                b = fis.read();
            }

            // 9) Blocking sleep on request thread (PERF)
            try {
                Thread.sleep(2000); // unnecessary blocking
            } catch (InterruptedException e) {
                // ignored
            }

            // 10) Insecure random used for token (SECURITY) — using SecureRandom but used incorrectly below
            byte[] token = new byte[16];
            new SecureRandom().nextBytes(token);
            String tok = Arrays.toString(token);
            if (rememberMe) {
                // pretend to set cookie; not HttpOnly, insecure
                System.out.println("Set-Cookie: rem=" + tok + "; Path=/;"); // insecure logging
            }

        } catch (Exception e) {
            // overly broad catch, swallowing exceptions (CODING + DEBUGGABILITY)
            System.out.println("Something bad happened: " + e.getMessage());
        } finally {
            // Improper resource cleanup (some closed, some not; no try-with-resources)
            try {
                if (stmt != null) stmt.close();
            } catch (Exception ex) {}
            try {
                if (conn != null) conn.close();
            } catch (Exception ex) {}
            // fis not closed intentionally — resource leak remains
        }

        return res;
    }

    // Bad helper: MD5 hashing (SECURITY)
    public static String md5(String s) {
        try {
            MessageDigest d = MessageDigest.getInstance("MD5");
            byte[] bs = d.digest(s.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : bs) sb.append(Integer.toHexString(0xff & b));
            return sb.toString();
        } catch (Exception e) {
            return "";
        }
    }

    // Example of public mutable field and poor naming
    public List<String> publicList = new ArrayList<>();

    // A synchronized method that synchronizes on a public object (THREAD SAFETY issue)
    public synchronized void addToList(String v) {
        publicList.add(v); // synchronized method but list still exposed
    }

    // Dead code and TODOs left in production
    // TODO: implement role-based access check
    private void unusedMethod() {
        // commented out dangerous code
        // System.exit(0);
    }
}
