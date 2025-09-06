import os
import training
import testing

def user_command():
    options = {
                1: "Detect images ",
                2: "Train your model ",
                3: "Most recent model",
                4: "Exit()"
                }
    
    stop = False
    while stop == False:
        for key, value in options.items():
            print(f"{key} : {value}")
        command_no = input("Select a option: ")
        try:
            command_no = int(command_no)
        except:
            print("Command has to to integer.")
            pass
        if command_no not in options:
            print("Enter a valid option.")
        else:
            if command_no == 1:
                test_images = testing.read_test_files()
                model = testing.load_model()
                for image in test_images:
                    testing.detect(model=model, image=image)
            elif command_no == 2:
                training.train_model()  
            elif command_no == 3:
                most_recent_model_path = training.most_recent_model()
                print(f"""
                      last trained model is {most_recent_model_path.split('/')[-5]}
                      That model had max train file named, {most_recent_model_path.split('/')[-3]}
                      the path to the most recent model is:
                                                            {most_recent_model_path}
                                                            
                                                            """)
            elif command_no == 4:
                print("""
                            HAVE A NICE DAY!!!
                            
                            """)
                break
                
                
                
user_command()