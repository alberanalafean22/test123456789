import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://drive.google.com/file/d/1IhyFeTISaJBNQbQXsckcs-29JB3kMKXd/view?usp=drive_link");   

             background-size:   
 cover;
             background-position: top center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
# HTML code as a multi-line string
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>deeplearning13</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-size: cover;
            color: white;
            font-family: 'Roboto', sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        h1 {
            background-color: rgba(0, 128, 0, 0.8);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        
        }
        .upload-form {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        input[type="file"] {
            margin: 10px 0;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: white;
            color: black;
            font-size: 16px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: green;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: darkgreen;
        }
        img {
            margin-top: 20px;
            max-width: 100%;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>

    <h1>Deteksi Suara Burung di Taman Nasional Way Kambas</h1>
    
    <div class="upload-form">
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="audio" accept="audio/*" required>
            <input type="submit" value="Upload Audio">
        </form>
    </div>

    <div class="footer">
        <p>Kelompok 13 Deep Learning</p>
        <p>Prodi Sains Data, Fakultas Sains, Institut Teknologi Sumatera</p>
        <p>deeplearning13project@gmail.com</p>
    </div>

</body>
</html>
"""

# Display the HTML in Streamlit
st.components.v1.html(html_code, height=400, scrolling=True)

