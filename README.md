<h1 style="text-align: center;">Contact Book Management System</h1>
<p>Welcome to the Contact Book Management System project! This Command Line Interface (CLI) application allows users to manage their contact information using Python. The project implements Python programming concepts and ensures simplicity while adhering to a modular and reusable design.</p>
<h2>Features</h2>
<p><b>1. Add Contacts</b></p>
<ul>
  <li>Allows users to add a contact with details like:</li>
  <ul>
    <li><b>Name</b>, <b>Email</b>, <b>Phone Number</b>, <b>Address</b></li>
  </ul>
  <li><b>Prevents duplication of phone numbers.</b></li>
</ul>

<p><b>2. View Contacts</b></p>
<ul>
  <li><b>Displays all stored contacts in a user-friendly format.</b></li>
</ul>

<p><b>3. Save to File</b></p>
<ul>
  <li><b>Automatically saves contact information as a CSV file upon addition.</b></li>
</ul>

<p><b>4. Load from File</b></p>
<ul>
  <li><b>Loads all saved contacts when the program starts.</b></li>
</ul>

<p><b>5. Remove Contacts</b></p>
<ul>
  <li><b>Enables users to delete specific contacts by mobile number.</b></li>
</ul>

<p><b>6. Search Contact</b></p>
<ul>
  <li><b>Enables users to search specific contact by mobile number.</b></li>
</ul>

<h2>How to Run the Project</h2>
<ol>
  <li>Clone the repository</li>
  <li>Run the application: <code>python main.py</code></li>
</ol>

<h2>Key Highlights</h2>
<ul>
  <li><b>Modular design for better maintainability.</b></li>
  <li><b>Persistent storage ensures no data loss between sessions.</b></li>
  <li><b>Clear, user-friendly interface with meaningful error messages.</b></li>
</ul>

<h2>Design and File Structure</h2>

<h3>Application Design</h3>
<p>
The application is designed to follow a modular approach, where each Python file focuses on a specific functionality. 
This structure ensures maintainability, readability, and ease of debugging.
</p>

<h3>File Overview</h3>
<ul>
  <li><b>main.py</b>: Contains the interactive menu system for user interaction. It acts as the entry point for the application.</li>
  <li><b>add_contacts.py</b>: Handles adding and validating new contacts, ensuring no duplicate phone numbers are allowed.</li>
  <li><b>saving_into_file.py</b>: Save information into a csv file.</li>
  <li><b>view_contacts.py</b>: Manages the display of all stored contacts in a well-organized and user-friendly format.</li>
  <li><b>load_from_file.py</b>: Load data from csv file</li>
  <li><b>delete_contact.py</b>: Implements logic for deleting contacts based on user input.</li>
  <li><b>search.py</b>: Enables users to search for contacts using details such as Name, Email, or Phone Number.</li>
</ul>

<h3>Directory Structure</h3>
<pre>
ContactBookManagementSystem/
│
├── main.py
├── add_contacts.py
├── view_contacts.py
├── load_from_file.py
├── delete_contact.py
├── search.py
├── contact_file.csv        # File for storing contact data
├── saving_into_file     
├── application_design.pdf   # Visual representation of the application design
└── README.md
</pre>

<h2>Usage</h2>

<p>On running the program, you'll see a menu with the following options:</p>

<pre>
Welcome To Contact Book Management System
Enter 1 for Add Contacts
Enter 2 for View Contacts
Enter 3 for Delete Contacts
Enter 4 for Search Contacts
Enter 5 for Exit
</pre>

<p>Select an option by entering the corresponding number.</p>
<p>Follow the on-screen instructions to perform actions.</p>




