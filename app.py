from file_manager.file_manager import file_zipper, file_unzipper


def main():
    function_selection = input(
        str('What would you like to do? (Zip or Unzip): '))

    if function_selection == 'Zip':
        file_path = input(str('Enter the Original File Path: '))
        zip_path_name = input(str('Enter the Destination File Path: '))

        file_zipper(file_path, zip_path_name)

        print('Files Zipped!')

    elif function_selection == 'Unzip':
        file_path = input(str('Enter the Original File Path: '))
        destination_path_name = input(str('Enter the Destination Path: '))
        file_status = input(str('Please Enter a Status (r or w): '))

        file_unzipper(file_path, file_status, destination_path_name)

        print('Files Unzipped!')

    else:
        print('Please Enter a Valid Choice.')


if __name__ == "__main__":
    main()
