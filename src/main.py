import interface as i # Import the interface module and alias it as i

def run():
    """
    Function to run the YouTube downloader application.
    
    This function calls the set_user_interface function from the interface module
    to start the user interface of the application.
    
    Args:
        None
        
    Returns:
        None
    """
    i.set_user_interface() # Call the set_user_interface function

if __name__ == '__main__':
    """
    Entry point of the application.
    
    If this script is executed directly (not imported as a module),
    the run function is called to start the application.
    """
    run() # Call the run function to start the application