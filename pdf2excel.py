import PyPDF2
import pandas as pd

def should_ignore(line):
    return line.startswith('Page') and 'Factiva' in line
# Open the PDF file
with open('D:/AA econ/research track/articles/goolsbee test/goolsbee v1.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Initialize a list to store each row of data
    data = []
    all_lines = []

    # Loop through each page in the PDF
    for page in reader.pages:
        text = page.extract_text()
        text = text.replace('Allrightsreserved.', 'Allrightsreserved.\n')
        # print(text)
        lines = text.split('\n')
        all_lines.extend([line for line in lines if not should_ignore(line)])
    # print(all_lines)
    # df2 = pd.DataFrame(all_lines)
    # df2.to_excel('D:/AA econ/research track/articles/goolsbee test/test2.xlsx', index=False)

    # Process each line
    for i, line in enumerate(all_lines):
        if 'ReutersNews' in line or 'DowJonesInstitutionalNews' in line or 'TheWallStreetJournal' in line or 'BusinessInsider' in line or'WSJNewsletters'in line or 'Reuters News' in line or 'Dow Jones Institutional News' in line or 'The Wall Street Journal' in line or 'Business Insider' in line or'WSJ Newsletters'in line:
                # Split the line into components based on the structure
            parts = line.split(',')
                # if len(parts) > 3:  # Check if the line has enough parts
                #     # Append the data (customize the indices as per the actual structure)
                #     data.append([parts[0], parts[1], parts[2], ' '.join(parts[3:])])
            if i >= 3:
                    # 检查前三行是否以'Document'开头
                if all_lines[i - 3].startswith('Document'):
                        # 如果是，结合前两行
                    title = all_lines[i - 2] + all_lines[i - 1]
                else:
                        # 否则，只储存前一行
                    title = all_lines[i - 1]
            else:
                title = all_lines[i - 1]
                # data.append(title)
            for j in range(i + 1, len(all_lines)):
                if all_lines[j].startswith('Document'):
                    content = ''.join(all_lines[i + 1:j])
                        # data.append([content,all_lines[j]])
                    break
            if len(parts) > 3:  # Check if the line has enough parts
                    # Append the data (customize the indices as per the actual structure)
                data.append([parts[0], parts[1], parts[2], ' '.join(parts[3:]), title, content, all_lines[j]])
# Create a DataFrame
df = pd.DataFrame(data, columns=['Title', 'Time', 'Date', 'Unknow', 'Title', 'Content', 'Document'])

# #========================================================================================================================
# import PyPDF2
# import pandas as pd
#
# # Function to check if the line should be ignored
# def should_ignore(line):
#     return line.startswith('Page') and 'Factiva' in line
#
# # Function to check if the line contains news source
# def contains_news_source(line):
#     sources = ['ReutersNews', 'DowJonesInstitutionalNews', 'TheWallStreetJournal']
#     return any(source in line for source in sources)
#
# # Open the PDF file
# with open('D:/AA econ/research track/articles/goolsbee test/headline format-1.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     text = []
#
#     # Extract text from each page
#     for page in reader.pages:
#         page_text = page.extract_text()
#         lines = page_text.split('\n')
#
#         # Process each line
#         for i, line in enumerate(lines):
#             if not should_ignore(line):
#                 if 'marker_for_blue_text' in line:  # This is a placeholder condition
#                     # Assuming the blue text can be one or two lines
#                     sample = line
#                     if i + 1 < len(lines) and 'marker_for_blue_text' in lines[i + 1]:
#                         sample += ' ' + lines[i + 1]
#
#                     # Check the next lines for news source
#                     j = i + 1
#                     while j < len(lines) and not contains_news_source(lines[j]):
#                         j += 1
#                     if j < len(lines):
#                         news_line = lines[j].split(',')
#                         # Create a DataFrame or append to an existing DataFrame
#                         df = pd.DataFrame([{
#                             'sample': sample,
#                             'source': news_line[0],
#                             'time': news_line[1],
#                             'date': news_line[2],
#                             'word_count': news_line[3],
#                             'language': news_line[4]
#                         }])
#                         print(df)  # Or append to an existing DataFrame
#
# # You can now manipulate the DataFrame `df` as needed
# # Write DataFrame to Excel
df.to_excel('D:/AA econ/research track/articles/goolsbee test/goolsbeev1.xlsx', index=False)

print('PDF data has been written to Excel.')