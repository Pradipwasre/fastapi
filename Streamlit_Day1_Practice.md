# Streamlit Day 1 - Beginner Practice

## Goal

Learn Streamlit one command at a time, then build a simple Machine
Learning UI.

## Run Every Program

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 1. Import Streamlit

``` python
import streamlit as st
```

**What happens?** - Imports the Streamlit library. - `st` is the
shortcut name.

------------------------------------------------------------------------

## 2. Title

``` python
import streamlit as st

st.title("Hello World")
```

**New command:** `st.title()`

------------------------------------------------------------------------

## 3. Subheader

``` python
import streamlit as st

st.title("Hello World")
st.subheader("Welcome Students")
```

**New command:** `st.subheader()`

------------------------------------------------------------------------

## 4. Markdown

``` python
import streamlit as st

st.title("Hello World")
st.subheader("Welcome Students")
st.markdown("Today we are learning **Streamlit**.")
```

**New command:** `st.markdown()`

------------------------------------------------------------------------

## 5. Write

``` python
import streamlit as st

st.title("Hello World")
st.write("This is normal text.")
```

**New command:** `st.write()`

------------------------------------------------------------------------

## 6. Button

``` python
import streamlit as st

st.title("Button Example")

if st.button("Click Me"):
    st.write("Button Clicked!")
```

**Important:** `st.button()` returns `True` only when clicked.

------------------------------------------------------------------------

## 7. Multiple Buttons

``` python
import streamlit as st

st.title("Buttons")

st.button("Save")
st.button("Delete")
st.button("Reset")
```

------------------------------------------------------------------------

## 8. Text Input

``` python
import streamlit as st

name = st.text_input("Enter Your Name")

st.write(name)
```

------------------------------------------------------------------------

## 9. Number Input

``` python
import streamlit as st

age = st.number_input("Enter Age")

st.write(age)
```

------------------------------------------------------------------------

## 10. Slider

``` python
import streamlit as st

rating = st.slider("Rate this App", 1, 5)

st.write(rating)
```

------------------------------------------------------------------------

## 11. Select Box

``` python
import streamlit as st

city = st.selectbox(
    "Choose City",
    ["Pune", "Mumbai", "Delhi"]
)

st.write(city)
```

------------------------------------------------------------------------

## 12. Checkbox

``` python
import streamlit as st

agree = st.checkbox("I Agree")

st.write(agree)
```

------------------------------------------------------------------------

## 13. Radio Button

``` python
import streamlit as st

gender = st.radio(
    "Select Gender",
    ["Male", "Female"]
)

st.write(gender)
```

------------------------------------------------------------------------

## 14. Success Message

``` python
import streamlit as st

st.success("Login Successful!")
```

------------------------------------------------------------------------

## 15. Error Message

``` python
import streamlit as st

st.error("Wrong Password!")
```

------------------------------------------------------------------------

## 16. Warning Message

``` python
import streamlit as st

st.warning("Please Enter All Details")
```

------------------------------------------------------------------------

## 17. Info Message

``` python
import streamlit as st

st.info("Today's Class is on Streamlit.")
```

------------------------------------------------------------------------

# Final Practice - Simple ML UI

``` python
import streamlit as st

st.title("🛒 Blinkit Price Predictor")

name = st.text_input("Product Name")

weight = st.number_input("Weight")

rating = st.slider("Rating", 1, 5)

category = st.selectbox(
    "Category",
    ["Snacks", "Milk", "Fruits"]
)

if st.button("Predict Price"):
    st.success("Prediction Completed!")
```

## Commands Learned

-   st.title()
-   st.subheader()
-   st.markdown()
-   st.write()
-   st.button()
-   st.text_input()
-   st.number_input()
-   st.slider()
-   st.selectbox()
-   st.checkbox()
-   st.radio()
-   st.success()
-   st.error()
-   st.warning()
-   st.info()

## Homework

1.  Create your own profile page.
2.  Add your name, age, city, and a Submit button.
3.  Change the title and experiment with different widgets.

Happy Coding! 🚀
