# Email Attachment Downloader Module



# Import libraries and other modules
import sys
import os
import json
import email
import imaplib
import mysql_helper


# Main function
def download_attachments(directory, json_user_input, employee_code):
    try:
        # Define and initialize variables
        email_template = dict()
        mail_count = 0
        file_count = 0
        total_file_count = 0
        i1 = 0
        i2 = 0

        directory = '/var/sites/dev.***.net/python/qb_db_manager/payment_csv_files/' # temporary overwrite of directory; remove in live version

        # Delete all existing files in directory that belong to user
        for file_name in os.listdir(directory):
            if file_name[:3] == employee_code:
                os.remove(directory + file_name)

        # Convert JSON user input string to dictionary
        dict_user_input = json.loads(json_user_input)['user_input']

        # Handle front-end errors
        if not dict_user_input['template_name']:
            error_message = 'template_name is missing.'
            success_message = ''
            return error_message, success_message

        # Retrieve email template from database
        mysql_status1, mysql_message1, results1 = mysql_helper.mysql_select('pdf_parser_templates', ['*'], {'template_name' : dict_user_input['template_name']})
        mysql_status2, mysql_message2, results2 = mysql_helper.show_columns('pdf_parser_templates')
        for i0 in range(0, len(results2)):
            email_template.update({results2[i0][0] : results1[0][i0]})

        # Log into Gmail server, download emails from specified label, and handle IMAP errors
        try:
            mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
            mailbox.login('***', '***')
            mailbox.select("\"" + email_template['email_label'] + "\"")
            if email_template['sender_name'] != '':
                email_batch_type, email_batch_data = mailbox.search(None, 'From', "\"" + email_template['sender_name'] + "\"")
            else:
                email_batch_type, email_batch_data = mailbox.search(None, 'All')
        except mailbox.error as imap_error:
            error_message = 'IMAP Error: ' + str(imap_error)
            success_message = ''
            return error_message, success_message

        # Iterate through downloaded emails and capture message
        for email_item in email_batch_data[0].split():
            try:
                email_type, email_data = mailbox.fetch(email_item, '(RFC822)')
            except mailbox.error as imap_error:
                error_message = 'IMAP Error: ' + str(imap_error)
                success_message = ''
                return error_message, success_message

            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            message = email.message_from_string(raw_email_string)
            subject = message['subject']

            # Iterate through message attachments and save if they match template rules
            for attachment in message.walk():
                if attachment.get_content_maintype() == 'multipart':
                    continue    # skip current round
                if attachment.get('Content-Disposition') is None:
                    continue    # skip current round
                file_name = attachment.get_filename()
                if email_template['subject_keyword'] != '':
                    if subject.rfind(email_template['subject_keyword']) != -1:
                        if email_template['file_extension'] != '':
                            if file_name[-3:] == email_template['file_extension'] != '':
                                if email_template['filename_keyword'] != '':
                                    if file_name.rfind(email_template['filename_keyword']) != -1:
                                        file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                        file.write(attachment.get_payload(decode=True))
                                        file.close()
                                        file_count += 1
                                else:
                                    file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                    file.write(attachment.get_payload(decode=True))
                                    file.close()
                                    file_count += 1
                        else:
                            if email_template['filename_keyword'] != '':
                                if file_name.rfind(email_template['filename_keyword']) != -1:
                                    file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                    file.write(attachment.get_payload(decode=True))
                                    file.close()
                                    file_count += 1
                            else:
                                file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                file.write(attachment.get_payload(decode=True))
                                file.close()
                                file_count += 1
                else:
                    if email_template['file_extension'] != '':
                        if file_name[-3:] == email_template['file_extension'] != '':
                            if email_template['filename_keyword'] != '':
                                if file_name.rfind(email_template['filename_keyword']) != -1:
                                    file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                    file.write(attachment.get_payload(decode=True))
                                    file.close()
                                    file_count += 1
                            else:
                                file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                file.write(attachment.get_payload(decode=True))
                                file.close()
                                file_count += 1
                    else:
                        if email_template['filename_keyword'] != '':
                            if file_name.rfind(email_template['filename_keyword']) != -1:
                                file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                                file.write(attachment.get_payload(decode=True))
                                file.close()
                                file_count += 1
                        else:
                            file = open(directory + employee_code + '_mail_' + str(mail_count) + '_file_' + str(file_count) + '.pdf', 'wb')
                            file.write(attachment.get_payload(decode=True))
                            file.close()
                            file_count += 1

                # Safeguard for infinite attachment loop
                i1 += 1
                if i1 > 500:
                    error_message = 'Attachment loop count exceeded safeguard size of 500.'
                    success_message = ''
                    return error_message, success_message

            # Update counters
            total_file_count += file_count
            file_count = 0
            mail_count += 1

            # Safeguard for infinite email loop
            i2 += 1
            if i2 > 500:
                    error_message = 'Email loop count exceeded safeguard size of 500.'
                    success_message = ''
                    return error_message, success_message

        # Log out of Gmail server and handle any potential errors
        try:
            mailbox.close()
            mailbox.logout()
        except mailbox.error as imap_error:
            error_message = 'IMAP Error: ' + str(imap_error)
            success_message = ''
            return error_message, success_message

        # Return success message if no errors
        error_message = ''
        success_message = str(total_file_count) + ' email attachment(s) downloaded.'
        return error_message, success_message

    # Handle Python errors
    except Exception as py_error:
        error_type, error_object, error_traceback = sys.exc_info()
        error_message = 'Py Error @ Line #' + str(error_traceback.tb_lineno) + ': ' + str(py_error)
        success_message = ''
        return error_message, success_message


# Execute main funciton and return message
directory = '/var/sites/files/pdf_parser_files/'
json_user_input = sys.argv[1]
employee_code = sys.argv[2]
error_message, success_message = download_attachments(directory, json_user_input, employee_code)
print(json.dumps({'error_message' : error_message, 'success_message' : success_message}))