from PIL import Image, ExifTags, TiffImagePlugin, ImageOps

def scrape_exif(image):
    """
    Takes in a JPG binary.
    Returns a dict containing EXIF image metadata:
    { tag_name : tag_value }
    """
    # img = Image.open("sample.jpg")
    # img_exif = img.getexif()

    img = Image.open(image)
    img_exif = img.getexif()

    metadata = {}
    if img_exif is None:
        return metadata
    else:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                if isinstance(val, (TiffImagePlugin.IFDRational)):
                    metadata[ExifTags.TAGS[key]] = float(val)
                elif isinstance(val, (bytes)):
                    pass
                else:
                    metadata[ExifTags.TAGS[key]] = val
            else:
                print(f'{key}:{val}')
                metadata[key] = val

    return metadata


def convert_to_PIL_image(image_binary):
    """ Takes in an image binary and returns a PIL Image object """

    return Image.open(image_binary)


def convert_monochrome(image):
    """ Takes in a PIL Image, returns PIL Image in black and white """

    return image.convert("L")

def transpose(image):
    """ Transposes an image based on int's EXIF data.
    Takes image (PIL Image)
    """

    return ImageOps.exif_transpose(image)
