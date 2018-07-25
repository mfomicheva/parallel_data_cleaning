from classifier import Classifier


def main():
    features_path = '/home/jesus/news-commentary-v13.de-en.tok.low.features.negative.out_1K'
    model_path = '/home/jesus/models/news-commentary.p'
    classifier = Classifier()
    classifier.load_model(model_path)
    for row in classifier.lazy_load(features_path):
        pred = classifier._classifier.predict_proba([row])
        print(pred[0][1])


if __name__ == '__main__':
    main()
