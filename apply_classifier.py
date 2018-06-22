from classifier import Classifier


def main():
    features_path = '/home/jesus/news-commentary-v13.de-en.tok.low.features.negative.out_1K'
    model_path = '/home/jesus/models/news-commentary.p'
    classifier = Classifier()
    features = classifier.load_features(features_path)
    classifier.load_model(model_path)
    predictions = classifier._classifier.predict(features)
    for pred in predictions:
        print(pred)


if __name__ == '__main__':
    main()
