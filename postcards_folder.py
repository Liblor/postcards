from postcards import Postcards
import sys
import os
import random
import ntpath


class FolderPlugin(Postcards):
    supported_ext = ['.jpg', '.jpeg', '.png']

    def get_img_and_text(self, payload, cli_args):
        if not payload.get('folder'):
            print("No folder set in configuration")
            exit(1)

        folder = self._make_absolute_path(payload.get('folder'))

        candidates = []
        for file in os.listdir(folder):
            for ext in self.supported_ext:
                if file.endswith(ext):
                    candidates.append(file)

        if not candidates:
            print("No images in folder " + folder)
            exit(1)

        img_name = random.choice(candidates)
        img_path = os.path.join(folder, img_name)
        file = open(img_path, 'rb')

        if payload.get('move'):
            self._move_to_sent(folder, img_path)

        return {
            'img': file,
            'text': ''
        }

    def _move_to_sent(self, picture_folder, image_path):
        sent_folder = os.path.join(picture_folder, 'sent')
        if not os.path.exists(sent_folder):
            os.makedirs(sent_folder)

        img_name = self._get_filename(image_path)
        sent_img_path = os.path.join(sent_folder, img_name)
        os.rename(image_path, sent_img_path)

    def _get_filename(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def _make_absolute_path(self, path):
        if not os.path.isabs(path):
            abs_dir = os.path.dirname(os.path.realpath(__file__))
            return os.path.join(abs_dir, path)
        else:
            return path


if __name__ == '__main__':
    FolderPlugin().main(sys.argv[1:])
