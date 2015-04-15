# Here at the top I am writing the examples so I know what the HTML should look like

# Example from my webpage. This is how the real life HTML should look.
#<div class="main_title">
#  <p>
#    Stage 2: How to Solve Problems
#  </p>
#</div>
#
#<div class="sub_title">  
#  Understanding a problem
#</div>
#
#<div class="sub_title_description">  
#  <p>
#    A computational problem is defined by a set of possible inputs and the desired outputs. The solution is a procedure that gives the desired outputs based on the inputs. The first rule in solving a problem is to understand the possible inputs.
#  </p>
#</div>



# This is what we want as output from the python. 
# A main title, like for a section in the course
# A sub titles with a header for a diffent parts of the main title.
# A description with notes for the sub title.
# In my example above. Main_Title = Stage 2: How to Solve Problems
#           Sub_Title = Understanding a problem
#           Description = The text between the <p> tags
#<div class="main_title">
# <p>
#   main_title
# </p>
#</div>
#<div class="sub_title">
# Sub_Title
#</div>
#<div class="sub_title_description">
# <p>
#   sub_title_description
# </p>
#</div>

# Start by setting the user data for that is unique to the webpage.

# This is a list of the sections I want to pass into the HTML template.
# There is a main title in index 0, a sub title in index 1 and a sub title description in index 2
# The text in this list can be changed depending on what I want to publish to the webpage.
# More list elements can be added if more sections are needed.

section_list = [['main_title 1','sub_title 1','sub_title_description 1'],
		['main_title 2','sub_title 2','sub_title_description 2'],
		['main_title 3','sub_title 3','sub_title_description 3'],
                ['main_title 4','sub_title 4','sub_title_description 4']]	

# The filename for the CSS for the website can be unique, so we are setting that here
# Enter the name of the CSS file below
filename_for_css = "project_style_updated.css"

# This function will create the head tags of the HTML file as well as setting the filename for the CSS file

def generate_html_head(href_for_css):
    html_head = '''
<!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" type="text/css" href="''' + filename_for_css  
    html_head_mid = '''">
</head>

<body>
'''
    html_head_full = html_head + html_head_mid
    return html_head_full

# This fucntion will create the end tags for the HTML file

def generate_html_end():
  html_end = '''

</body>
</html>'''
  return html_end 


# This is the loop that kicks off the generate HTML looping through for each section (list element). Our input is the section_list
# It initializes a variable that starts with the head of the HTML file as defined by fucntion generate_html_head
# It then loops through each element in the section list and calls functions extract_list and in turn generate_html_section to create HTML for each section
# It then adds the newly created HTML for that section to the head or the other sections previously created
# Once it reaches the end of the section list the loop exits and we add the HTML end tags by calling generate_end_html and appending it to our generated HTML
# Then we return the HTML for all sections including the head and end to the print statement that called it.

def section_loop (section_list):					  
	all_html = generate_html_head(filename_for_css)									            
	for section in section_list:					    
		section_HTML = extract_list(section)		
		all_html = all_html + section_HTML      
	all_html = all_html + generate_html_end()	
	return all_html                           
	
# This function will extract the titles and description and pass it to generate_html_section
# Our input is one section from section_list from the section_loop function
# It extracts the index 0,1 and 2 from each list element and sets that as variables it passes to generate_html_section
# It then passes all these extracted elements to generate_html_section to create the HTML code for one section

def extract_list (section):					     
	main_title = section[0]					       
	sub_title  = section[1]					       
	sub_title_description = section[2]		 
	return generate_html_section (main_title,sub_title,sub_title_description) 

# This function will take 3 inputs and output them into a 'section' of HTML per my website design. 
# The inputs are generated from the extract_list function
# The formatting/indentation in this function shouldnt be changed

def generate_html_section(main_title,sub_title,sub_title_description):
        html_text_1 = '''
<div class="main_title">
  <p>
    ''' + main_title
        html_text_2 = '''
  </p>
</div>
<div class="sub_title">
    ''' + sub_title
        html_text_3 = '''
</div>
<div class="sub_title_description">
  <p>
    ''' + sub_title_description
        html_text_4 = '''
  </p>
</div>'''
        full_section_html = html_text_1 + html_text_2 + html_text_3 + html_text_4
        return full_section_html	

# This final line prints out the full HTML code for all sections defined in section_list with our free text inside the sections. As well as the head and end of the HTML file.
print section_loop(section_list)
