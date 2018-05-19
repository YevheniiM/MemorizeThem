# MemorizeThem

> There is no such thing as a 'self-made' man. We are made up of thousands of others. Everyone who has ever done a kind deed for us, or spoken one word of encouragement to us, has entered into the make-up of our character and of our thoughts, as well as our success.

> (с) George Matthew Adams

### About MemorizeThem
The main goal of my web application is to keep your **circle of friends** up to date. Always **be in touch** with people that you know and never forgot such things as birth date or some facts from their lives.

If you aren't sure in whether do you need this app or not: just think about your **social connections**. How much friends you have? 50? 200? 500? Do you remember all information about them? In what spheres they work? Or how many children they have? Whatever. With MemorizeThem you will know all this facts - the only thing that you need is desire.

Predictable question is "Why I should write all these facts about my **connetions**? And I have very simple answer - **to be connected**!

------------

### Google Contacts API

My web application uses the latest version of Google Contacts API.

The Google Contacts API allows client applications to view and update a user's contacts. Contacts are stored in the user's Google Account; most Google services have access to the contact list.

Your client application can use the Google Contacts API to create new contacts, edit or delete existing contacts, and query for contacts that match particular criteria

------------

### Structure

MemorizeThem consists of other smaller application, such as:
- **MemorizeThem** (the main application, which controls everything, includes basic urls and settings)
- **google_auth** (the application is needed to work with Google Contacts API and all the stuff connected with it)
- **models_test** (the application works with models, such as Contact model)
- **user_authorization** (the application is needed to register and authorize users)

------------

### Instructions

Some basic instructions, that you can follow to get strated with MemorizeThem.

1. Press [Login] to login in (if you are not registered, press the registration button at the login form)
2. Press [My friends] to see all your contacts.
3. Press [Import Contacts] to import contact from your gmail account.
4. Press [Create Contact] to create new contact.
5. Press [Delete All Contacts] to delete all your contacts.
6. Press [Sort by] and choose which filter you want to apply for your contacts to be sorted.
7. Press [Details] to see information details about your contacts.
8. Press [Delete] button on the details page to delete the contact.
9. Press [Edit] to edit the information about your contact.
10. Press [MemorizeThem] to return to the main page.