```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Pre-order</title>
    <style>
        /* Basic styling for demonstration purposes */
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1, h2, p {
            margin-bottom: 15px;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        .cta-button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Book Title</h1> 
        <h2>by Author Name</h2>

        <img src="book-cover.jpg" alt="Book Cover"> <br>

        <p>Short description of the book. This is where you entice readers with a glimpse into the story, characters, and themes without giving too much away.</p>

        <h2>Pre-order Now and Get:</h2>
        <ul>
            <li>Bonus Content</li>
            <li>Early Access</li>
            <li>Special Discount</li>
        </ul>

        <a href="#" class="cta-button">Pre-order Now</a>
    </div>

    <script>
        // You can add JavaScript functionality here for form handling, 
        // pre-order validation, interaction with a backend service, etc. 
        // For this example, we'll keep it simple with just the HTML structure.
    </script>
</body>
</html>
```

**Explanation:**

- **HTML Structure:**
    - We use a basic HTML structure with a `container` div to center the content.
    - `<h1>`, `<h2>`, and `<p>` tags are used for headings and paragraphs for the book information.
    - An `<img>` tag displays the book cover (replace `book-cover.jpg` with the actual filename).
    - A `<ul>` (unordered list) is used to list pre-order benefits.
    - The `<a>` tag with class `cta-button` creates the pre-order button.

- **CSS Styling:**
    - Basic CSS is provided within `<style>` tags to style the page. You can customize this further to match your book's design.

- **JavaScript (Optional):**
    - The `<script>` tags are included for adding JavaScript functionality. 
    - You can use JavaScript to:
        - Handle form submissions when a user clicks "Pre-order Now."
        - Validate user input (e.g., email address).
        - Send pre-order data to your backend server or third-party service.
        - Implement interactive elements on the page.

**How to Use This Code:**

1. **Replace Placeholders:**
   - Change `"Book Title"`, `"Author Name"`, `book-cover.jpg`, book description, and pre-order benefits with your actual content.
2. **Link Pre-order Button:**
   - Change the `href` attribute of the `<a>` tag from `"#"` to the actual URL where users can pre-order (e.g., an online store, your website's checkout page).
3. **Add JavaScript Functionality (Optional):**
   - Write JavaScript code within the `<script>` tags to implement form handling, validation, and any other interactive features.
4. **Test and Deploy:**
   - Test the page thoroughly in different browsers and devices to ensure it looks and works correctly.
   - Once you are happy with it, deploy the HTML file to your web server.

This code provides a basic framework for a book pre-order landing page. You can customize it further by adding more design elements, sections, social media links, and advanced functionality using JavaScript. 
