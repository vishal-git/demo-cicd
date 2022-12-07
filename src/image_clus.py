### read raw images from a folder and perform image clustering on them

from glob import glob
from PIL import Image
from sentence_transformers import SentenceTransformer, models
from utils import community_detection


def clus_images(img_dir):
    """
    Reads raw images from the input dir, resizes them identifies clusters
    """
    raw_img_files = glob(img_dir)
    n_raw_images = len(raw_img_files)
    print(f"{n_raw_images} images read from the input directory.")

    # load the clip model
    clip_model = models.CLIPModel()
    model = SentenceTransformer(modules=[clip_model])

    # resize raw images
    resized_images = []
    for raw_img_file in raw_img_files:
        raw_img = Image.open(raw_img_file)
        resized_img = raw_img.resize((224, 224))
        resized_images.append(resized_img)

    # create image embeddings
    img_emb = model.encode(resized_images, convert_to_tensor=True)

    # cluster images
    clus = community_detection(
        img_emb, threshold=0.8, min_community_size=2, init_max_size=5
    )
    print(f"Number of clusters identified: {len(clus)}")

    return n_raw_images, clus


if __name__ == "__main__":
    _, clusters = clus_images("./data/*")
    for cluster in clusters:
        print(cluster)
