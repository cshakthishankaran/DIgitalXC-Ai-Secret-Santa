
import openpyxl


class SecretSantaGenerator :

    pass

    def __init__(self, employee_list_filepath,previous_secret_santas_filepath):
       
       
      self.employees = self.read_xlsx(employee_list_filepath)
      self.previous_secret_santas = self.read_xlsx(previous_secret_santas_filepath)
      


    def read_xlsx(self, file_path):
        
        """
        Reads an Excel file and returns a list of dictionaries, where each row is a dictionary.
        
        :param file_path: Path to the Excel file
        :return: List of dictionaries representing the data in the Excel file

        """
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            headers = [cell.value for cell in sheet[1]]  # Read the header row
            data = []
            for row in sheet.iter_rows(min_row=2, values_only=True):  # Read from the second row
                data.append(dict(zip(headers, row)))
            return data
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return []










def letsPlaySecretSanta ():
  
  """
    Below are the files that need to be analysed for playing Secret Santa game.

    Files :

      1.  Employee_List.xlsx
      2.  Secret-Santa-Game-Result-2023.xlsx

  """

  employee_list_filepath = "Employee-List.xlsx"
  previous_secret_santas_filepath = "Secret-Santa-Game-Result-2023.xlsx"
  new_secret_santas_filepath = "Secret-Santa-Game-Result-2024.xlsx"



if __name__ == "__main__" :
  letsPlaySecretSanta()
