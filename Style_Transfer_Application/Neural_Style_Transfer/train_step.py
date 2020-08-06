import tensorflow as tf
from .style_content_loss import style_content_loss
from .clip_0_1 import clip_0_1


def train_step(image, extractor, opt, style_targets, content_targets, num_style_layers, num_content_layers):
    with tf.GradientTape() as tape:
        outputs = extractor(image)
        loss = style_content_loss(outputs, style_targets, content_targets, num_style_layers, num_content_layers)

    grad = tape.gradient(loss, image)
    opt.apply_gradients([(grad, image)])
    image.assign(clip_0_1(image))
