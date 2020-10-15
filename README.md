# alfred-worldanvil
An Alfred4 workflow to quickly open WorldAnvil articles for viewing or editing. This workflow will only search a single world at a time. It cannot currently be used to search all your worlds at once. I may add that functionality later, but it is also likely that I will not. :)

# IMPORTANT DISCLAIMER
This application relies on an unofficial, as-yet unsupported API. It is liable to break at any moment. More importantly, if you do not already have your very own API key, I cannot help you nor tell you how to get one. I will update this README if any of this changes, but for now, this should be considered use-at-your-own-risk. 

## Preparation
You can either clone this repository on your local machine using:

`git clone https://github.com/vinceblake/alfred-worldanvil.git`

Or you can download the .zip file directly and extract it. 

Place the `wasearch.py` file somewhere safe. Anywhere you like is fine but it'll need to live there permanently. You'll also need to reference its location in a moment, so make sure you know where it is.

---

# Instructions
1. Open wasearch.py in your [text] editor of choice. 

2. Starting at line 4, there are three variables you will need to update

  * `world_id` refers to the ID of the world you want to search. You can retrieve this value by navigating to your world's Dashboard and checking its URL, which will look something like this: `https://www.worldanvil.com/world/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/summary`. That long alphanumeric string (represented by Xs in this example) is your world's ID. 

  * While on your Dashboard, click your profile picture in the upper right to expand the menu and choose **API Keys Management**. Again, this will not appear without a Grandmaster+ subscription level.

  * Choose a nickname for this application. It can be whatever you like. Click "Create new Key."

  * You will now see a very long alphanumeric string beneath the app title that you just chose. That string is your `xAuthKey` variable, so paste it in accordingly.

  * Lastly, you will need your API key. At the moment, these are private and not freely distributed. If you don't already have one, I can't tell you how to get one. Once you have one, though, it will be your `xAppKey` variable. 

  * Save your changes and, once again, note the file path where you've saved the .py file.

3. Double-click the .alfredworkflow file to import it directly into Alfred4. You will be prompted with a screen that includes something like this:

  ![img](https://github.com/vinceblake/alfred-worldanvil/blob/main/script_path.png)

4. Double-click the field to the right of `script_path` to paste in--you guessed it--the path to your `wasearch.py` file. Mine, for example, is `/users/vince/Code/alfred-worldanvil/wasearch.py`. I recommend you avoid having spaces anywhere in that path.

5. By default, `ao` will be used to open an article for viewing and `ae` will be used to open it for editing. You can set these to whatever you like. 
