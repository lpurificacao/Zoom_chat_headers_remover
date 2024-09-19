import os  # https://docs.python.org/3/library/os.html#module-os
import fnmatch  # https://docs.python.org/3/library/fnmatch.html
import emoji  # https://pypi.org/project/emojis/


def main():
    clean_chat = 'last-chat-cleared-of-headers.txt'
    ext_type = '*.txt'

    def most_recent_file(directory):
        '''Iterates through the current directory and finds the most recent file base on its modification time.
        It then removes the headers and emojis added in the file by Zoom'''
        last_modified_time = 0
        for dir_path, dir_name, file_name in os.walk(directory):
            files = [file for file in fnmatch.filter(file_name, ext_type) if file != clean_chat]
            for file in files:
                file_path = os.path.join(dir_path, file)
                # Gets the modification time, a floating-point number giving the number of seconds since the epoch
                file_modified_time = os.path.getmtime(file_path)
                # the condition below makes the last_modified_time replace the initial value 0
                # the cycle keeps replacing last_modified_time if the date/time of each file is lower
                # if it's higher, the last_modified_time will not assume the date/time of that file
                if file_modified_time > last_modified_time:
                    last_modified_time = file_modified_time
                    last_modified_file = file_path

        return last_modified_file

    def get_rid_of_headers_and_emojis():
        file_path = most_recent_file(os.getcwd())

        def is_char_emoji(character):
            return character in emoji.EMOJI_DATA

        def text_has_emoji(text):
            for character in text:
                if is_char_emoji(character):
                    return True
            return False

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = []
            for line in file:
                # Get the lines starting with a tab and not containing emojis
                if line.startswith('\t') and not text_has_emoji(line):
                    file_content.append(line.strip())  # Stripping whitespace
        return file_content

    def chat_to_txt():
        clean_content = get_rid_of_headers_and_emojis()
        with open(clean_chat, 'w') as file:
            for index in clean_content:
                file.write(f'{index}\n')
                print(index)
        print(f'\nZoom chat was cleaned and written to "{clean_chat}"')

    chat_to_txt()


if __name__ == '__main__':
    main()
