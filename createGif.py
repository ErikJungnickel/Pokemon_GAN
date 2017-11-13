import imageio
import os

def createGif(filenames):
    images = []
    for filename in filenames:
        images.append(imageio.imread('./newPokemon/' + filename))
    imageio.mimsave('./pokemon.gif', images)


if __name__ == "__main__":
    filenames = os.listdir('./newPokemon/')    
    createGif(filenames)
