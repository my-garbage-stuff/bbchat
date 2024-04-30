#!/bin/sh

# Set content type header
echo "Content-type: text/html"
echo ""

# HTML header
echo "<html><head><title>CGI Example</title></head><body>"

# Check if the request method is POST
if [ "$REQUEST_METHOD" = "POST" ]; then
    # Read input from standard input (POST data)
    read QUERY_STRING

    # Extract the value of the input field named "data"
    data=$(echo "$QUERY_STRING" | grep -oP "(?<=data=)[^&]*")

    # Write the data to a file
    echo "$REMOTE_ADDR: $data" >> messages

    # Output success message
    echo '<meta http-equiv="refresh" content="0; url=/send.cgi" />'
else
    # Output form if the request method is not POST
    echo "<form method='post' action='$SCRIPT_NAME'>"
    echo "<input type='text' name='data'>"
    echo "<input type='submit' value='Submit'>"
    echo "</form>"
fi

# HTML footer
echo "</body></html>"
