from common_information import CommonInformation
import os

def main(pathToFile : str):
    common_informaion = CommonInformation(pathToFile)
    common_informaion.assign_common_inforamtion()
    
if __name__ == "__main__":
    pathToFile : str = "/home/rena/30-01EKLU1A25-E01.pdf"
    if os.path.exists(pathToFile):
        main(pathToFile)