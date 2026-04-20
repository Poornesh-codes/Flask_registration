# Flask registration app
this is simple registration form tht takes a username,email,and pass word checks if they are vald and saves them to database

## what i learned
- @app.route connects url to a python functions. it triggers the function when the url is called.
- render_template finds the html file and then passes variables into  it 
- validate_on_submit() -  when i submit, the parameters it validates if all field are macthing correctly
- db.session.add() keeps it ready to add the data into the sqlite db and db.session.commit() commits the changes to the database
- form.hidden_tag() - it generates a a random key along with the form , while submittion of form it checks for if the key matches and then accepts the form
-  using bootstrap for nav 
## challenges i faced
- form.hidden_tag() was not added ,the form was not submitting
- email-validator was needed to install separately

## testing
- length of password is short
![length of password](<Screenshot 2026-04-20 120227.png>)
- confirm password did not match with password
![confirm password](<Screenshot 2026-04-20 120256.png>)
- not a valid email 
![invalid](<Screenshot 2026-04-20 120449.png>)
![not an email](<Screenshot 2026-04-20 120524.png>)
- if everything is valid
![everything right](<Screenshot 2026-04-20 120401.png>)
## how to run 
pip install requirements.txt
python app.py

