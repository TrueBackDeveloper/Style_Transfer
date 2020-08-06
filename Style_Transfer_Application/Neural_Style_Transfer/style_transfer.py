import tensorflow as tf
from .load_img import load_img
from .style_content_model import style_cotent_model
from .train_step import train_step
from .tensor_to_image import tensor_to_image


def style_transfer(content_path, style_path, epochs):
    content_layers = ['block5_conv2']

    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1',
                    'block4_conv1',
                    'block5_conv1']

    num_content_layers = len(content_layers)
    num_style_layers = len(style_layers)

    extractor = style_cotent_model(style_layers, content_layers)

    content_image = load_img(content_path)
    style_image = load_img(style_path)

    style_targets = extractor(style_image)['style']
    content_targets = extractor(content_image)['content']
    opt = tf.optimizers.Adam(learning_rate=0.02, beta_1=0.99, epsilon=1e-1)
    image = tf.Variable(content_image)

    steps_per_epoch = 100
    step = 0
    for n in range(epochs):
        for m in range(steps_per_epoch):
            step += 1
            train_step(image, extractor, opt, style_targets, content_targets, num_style_layers, num_content_layers)

    tensor_to_image(image).save('./media/images/stylized-image.png')
