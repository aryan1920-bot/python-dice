import streamlit as st
from PIL import Image
import random

def roll_dice():
    num = random.randint(1, 6)
    return num

def get_dice_image(num):
    images = {
        1: 'dice1.png',
        2: 'dice2.png',
        3: 'dice3.png',
        4: 'dice4.png',
        5: 'dice5.png',
        6: 'dice6.png'
    }
    image_path = images.get(num)
    if image_path:
        return Image.open(image_path)

def main():
    st.title('Dice Roller')
    if st.button('Roll the Dice'):
        result = roll_dice()
        st.write(f"Result: {result}")
        dice_image = get_dice_image(result)
        if dice_image:
            st.image(dice_image, use_column_width=True)

if __name__ == '__main__':
    main()
