PLACE_HOLDER = "[name]"

with open('\Mail Merge Project Start\Input\Names\invited_names.txt') as invited_name:
    name = invited_name.readlines()


with open('\Mail Merge Project Start\Input\Letters\starting_letter.txt') as file:
    file_content = file.read()
    for first_names in name:
        stripped_name = first_names.strip()
        new_letter = file_content.replace(PLACE_HOLDER, stripped_name)
        with open(f"\Mail Merge Project Start\Output\ReadyToSend\lettter_for_{new_letter}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)