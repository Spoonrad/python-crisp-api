##
# python-crisp-api
#
# Copyright 2018, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class WebsiteResource(object):
  def __init__(self, parent):
    self.parent = parent

  def __url_website(self, website_id, resource):
    return "/website/%s%s" % (website_id, resource)

  def __url_conversation(self, website_id, session_id, resource):
    return self.__url_website(website_id, "/conversation/%s%s" % (session_id, resource))

  def __url_people(self, kind, website_id, people_id, resource):
    return self.__url_website(website_id, "/people/%s/%s%s" % (kind, people_id, resource))

  def create_website(self, data):
    return self.parent.post("/website", data)

  def get_website(self, website_id):
    return self.parent.get(self.__url_website(website_id, ""))

  def delete_website(self, website_id):
    return self.parent.remove(self.__url_website(website_id, ""))

  def batch_resolve_items(self, website_id, data):
    return self.parent.patch(self.__url_website(website_id, "/batch/resolve"), data)

  def batch_read_items(self, website_id, data):
    return self.parent.patch(self.__url_website(website_id, "/batch/read"), data)

  def batch_remove_items(self, website_id, data):
    return self.parent.patch(self.__url_website(website_id, "/batch/remove"), data)

  def get_website_availability_status(self, website_id):
    return self.parent.get(self.__url_website(website_id, "/availability/status"))

  def list_website_operators(self, website_id):
    return self.parent.get(self.__url_website(website_id, "/operators/list"))

  def list_last_active_website_operators(self, website_id):
    return self.parent.get(self.__url_website(website_id, "/operators/active"))

  def get_website_settings(self, website_id):
    return self.parent.get(self.__url_website(website_id, "/settings"))

  def update_website_settings(self, website_id, data):
    return self.parent.patch(self.__url_website(website_id, "/settings"), data)

  def count_visitors(self, website_id):
    return self.parent.get(self.__url_website(website_id, "/visitors/count"))

  def list_visitors(self, website_id, page_number):
    return self.parent.get(self.__url_website(website_id, "/visitors/list/%d" % page_number))

  def list_conversations(self, website_id, page_number):
    return self.parent.get(self.__url_website(website_id, "/conversations/%d" % page_number))

  def create_new_conversation(self, website_id, data):
    return self.parent.post(self.__url_website(website_id, "/conversation"), data)

  def check_conversation_exists(self, website_id, session_id):
    return self.parent.head(self.__url_conversation(website_id, session_id, ""))

  def get_conversation(self, website_id, session_id):
    return self.parent.get(self.__url_conversation(website_id, session_id, ""))

  def remove_conversation(self, website_id, session_id):
    return self.parent.remove(self.__url_conversation(website_id, session_id, ""))

  def initiate_conversation_with_existing_session(self, website_id, session_id):
    return self.parent.post(self.__url_conversation(website_id, session_id, "/initiate"))

  def get_messages_in_conversation(self, website_id, session_id, query):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/messages"), query)

  def send_message_in_conversation(self, website_id, session_id, data):
    return self.parent.post(self.__url_conversation(website_id, session_id, "/message"), data)

  def update_message_in_conversation(self, website_id, session_id, fingerprint, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/message/%d" % fingerprint), data)

  def compose_message_in_conversation(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/compose"), data)

  def mark_messages_read_in_conversation(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/read"), data)

  def mark_messages_delivered_in_conversation(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/delivered"), data)

  def get_conversation_routing_assign(self, website_id, session_id):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/routing"))

  def assign_conversation_routing(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/routing"), data)

  def get_conversation_metas(self, website_id, session_id):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/meta"))

  def update_conversation_metas(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/meta"), data)

  def list_conversation_pages(self, website_id, session_id, page_number):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/pages/%d" % page_number))

  def list_conversation_events(self, website_id, session_id, page_number):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/events/%d" % page_number))

  def get_conversation_state(self, website_id, session_id):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/state"))

  def change_conversation_state(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/state"), data)

  def get_block_status_for_conversation(self, website_id, session_id):
    return self.parent.get(self.__url_conversation(website_id, session_id, "/block"))

  def block_incoming_messages_for_conversation(self, website_id, session_id, data):
    return self.parent.patch(self.__url_conversation(website_id, session_id, "/block"), data)

  def request_email_transcript_for_conversation(self, website_id, session_id, data):
    return self.parent.post(self.__url_conversation(website_id, session_id, "/transcript"), data)

  def get_people_statistics(self, website_id):
    return self.parent.get(self.__url_website(website_id, "/people/stats"))

  def list_people_segments(self, website_id, page_number):
    return self.parent.get(self.__url_website(website_id, "/people/segments/%d" % page_number))

  def list_people_profiles(self, website_id, page_number):
    return self.parent.get(self.__url_website(website_id, "/people/profiles/%d" % page_number))

  def search_people_profiles(self, website_id, page_number, search_filter):
    return self.parent.get(self.__url_website(website_id, "/people/profiles/{}?search_filter={}".format(page_number, search_filter)))

  def add_new_people_profile(self, website_id, data):
    return self.parent.post(self.__url_website(website_id, "/people/profile"), data)

  def check_people_profile_exists(self, website_id, people_id):
    return self.parent.head(self.__url_people("profile", website_id, people_id, ""))

  def get_people_profile(self, website_id, people_id):
    return self.parent.get(self.__url_people("profile", website_id, people_id, ""))

  def save_people_profile(self, website_id, people_id, data):
    return self.parent.put(self.__url_people("profile", website_id, people_id, ""), data)

  def update_people_profile(self, website_id, people_id, data):
    return self.parent.patch(self.__url_people("profile", website_id, people_id, ""), data)

  def remove_people_profile(self, website_id, people_id):
    return self.parent.remove(self.__url_people("profile", website_id, people_id, ""))

  def list_people_conversations(self, website_id, people_id, page_number):
    return self.parent.get(self.__url_people("conversations", website_id, people_id, "/list/%d" % page_number))

  def add_people_event(self, website_id, people_id, data):
    return self.parent.post(self.__url_people("events", website_id, people_id, ""), data)

  def list_people_events(self, website_id, people_id, page_number):
    return self.parent.get(self.__url_people("events", website_id, people_id, "/list/%d" % page_number))

  def get_people_data(self, website_id, people_id):
    return self.parent.get(self.__url_people("data", website_id, people_id, ""))

  def save_people_data(self, website_id, people_id, data):
    return self.parent.put(self.__url_people("data", website_id, people_id, ""), data)

  def get_people_subscription_status(self, website_id, people_id):
    return self.parent.get(self.__url_people("subscription", website_id, people_id, ""))

  def update_people_subscription_status(self, website_id, people_id, data):
    return self.parent.patch(self.__url_people("subscription", website_id, people_id, ""), data)
