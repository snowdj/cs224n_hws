import tensorflow as tf

import q2_parser_model

class Config(object):
    """Holds model hyperparams and data information.
    The config class is used to store various hyperparameters and dataset
    information parameters. Model objects are passed a Config() object at
    instantiation. They can then call self.config.<hyperparameter_name> to
    get the hyperparameter settings.
    """
    n_features = 36
    n_classes = 3
    dropout = 0.5  # (p_drop in the handout)
    embed_size = 50
    n_hidden_layers = 2
    hidden_size = 200
    batch_size = 1024
    n_epochs = 10
    lr = 0.0005
    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True

if __name__ == '__main__':
    q2_parser_model.main(debug=False, config=Config())