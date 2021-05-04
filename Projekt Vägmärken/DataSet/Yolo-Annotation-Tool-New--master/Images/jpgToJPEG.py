import os

path = 'C:/Users/harle/Documents/GitHub/ai-dataanalys-HarleyBerglund/Projekt Vägmärken/DataSet/Yolo-Annotation-Tool-New--master/Images/data'


def main():

    for filename in os.listdir(path):
        arr = filename.split(".")

        if arr[1] == "jpg":
            dst = arr[0] + ".JPEG"
            src = path + '/' + filename
            dst = path + '/' + dst

            os.rename(src, dst)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
