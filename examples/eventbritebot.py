import os
import time
import re
from slackbot.slackbot import SlackBot
from eventbrite import Eventbrite

# Create bot as subclass of SlackBot
class EventbriteBot(SlackBot):
  """
    A class for connecting to Eventbrite via Slack.
  """
  # constants
  WHAT_COMMAND = "what"
  ARE_COMMAND = "are"
  WHERE_COMMAND = "where"
  HOW_COMMAND = "how"

  def __init__(self, name):
    """
      name - name of the bot as registered with Slack
    """
    super(EventbriteBot, self).__init__(name)

  # Ovveride the command parser to add your own command handling
  def parse_commands(self, commands, channel):
    """
      Parses the comamand received from Slack.
      Initally calls the base class to handle default commands.
      Calls individual handler for each command group
    """
    response, attachments = super(EventbriteBot, self).parse_commands(commands, channel)

    if commands[0] == self.WHAT_COMMAND:
      response = "Here are the events I know about:\n"
      events = eventbrite.event_search(**{'user.id': user['id']})
      for event in events['events']:
        response = response + "(ID " + event['id'] + ") " + str(event['name']['text']) + " starting " + str(event['start']['local']) + "\n"

    if commands[0] == self.WHO_COMMAND:
      response, attachments = self.handle_who(commands)

    if commands[0] == self.HOW_COMMAND:
      if commands[1] == "many":
        attendees = eventbrite.get_event_attendees(commands[2])
        if "attendees" in attendees:
          response = "There are " + str(len(attendees['attendees'])) + " people attending:\n"

        else:
          response = "Sorry I don't know that event. Try *" + self.WHAT_COMMAND + "* to see list of events and their IDs"

    return response, attachments

  def handle_help(self, commands):
    """
      Process the help command

      Override the default handle_help to add your own help message
    """
    response, attachments = super(EventbriteBot, self).handle_help(commands)
    response += "*" + self.WHAT_COMMAND + "* - lists the events\n"
    response += "*" + self.WHO_COMMAND + " <id>* - lists who is attending event\n"
    response += "*" + self.HOW_COMMAND + " many <id>* - how many people attending event with <id>\n"

    return response, attachments

  def handle_who(self, commands):
    """
      Process the who command

      Override the default handle_who to add your own responses
    """
    response, attachments = super(EventbriteBot, self).handle_who(commands)

    if response == "":
      attendees = eventbrite.get_event_attendees(commands[1])
      if "attendees" in attendees:
        response = "Here are the people attending:\n"
        for attendee in attendees['attendees']:
          response = response + attendee['profile']['first_name'] + " " + attendee['profile']['last_name'] +  " " + attendee['profile']['email'] + " " + attendee['ticket_class_name'] + "\n"
      else:
        response = "Sorry I don't know that event. Try *" + self.WHAT_COMMAND + "* to see list of events and their IDs"

    return response, attachments

# Eventbrite's token as an environment variable
# Using the your token from Eventbrite, to set the environmant variable use:
# export EVENTBRITE_TOKEN='token'
EVENTBRITE_TOKEN = os.environ.get("EVENTBRITE_TOKEN")

# instantiate Eventbrite client
eventbrite = Eventbrite(EVENTBRITE_TOKEN)
user = eventbrite.get_user()

# instantiate SlackBot
slackbot = EventbriteBot("eventbot")

if __name__ == "__main__":
    slackbot.run()