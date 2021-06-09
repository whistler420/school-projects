from PIL import Image
src = Image.open('/home/whistler/import/bruh.png')
joke = Image.open('/home/whistler/import/bruh no 2.png')
src = src.resize((620,646))
joke = joke.convert("RGBA")
src.paste(joke, (20,20), joke)
src.save('funnyjoke.png')