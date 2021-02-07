#!/usr/bin/python
#
# Script to create KML with Google Contacts data.
#
# This is not working yet.

import gdata.auth
import gdata.contacts.client
import gdata.contacts.data

def PrintAllContacts(gd_client):
  feed = gd_client.GetContacts()
  for i, entry in enumerate(feed.entry):
    print '\n%s %s' % (i+1, entry.name.full_name.text)
    if entry.content:
      print '    %s' % (entry.content.text)
    # Display the primary email address for the contact.
    for email in entry.email:
      if email.primary and email.primary == 'true':
        print '    %s' % (email.address)
    # Show the contact groups that this contact is a member of.
    for group in entry.group_membership_info:
      print '    Member of group: %s' % (group.href)
    # Display extended properties.
    for extended_property in entry.extended_property:
      if extended_property.value:
        value = extended_property.value
      else:
        value = extended_property.GetXmlBlob()
      print '    Extended Property - %s: %s' % (extended_property.name, value)

def main():
  gd_client = gdata.contacts.client.ContactsClient(source='ContactsExporter')
  #PrintAllContacts(gd_client, options.oauth_requestor_id)
  PrintAllContacts(gd_client)

if __name__ == '__main__':
  main()
