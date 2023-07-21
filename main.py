import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from VKTools import VKTools
from tokens import acces_token, comunity_token

class BotInterface():
    def __init__(self, acces_token, comunity_token):
        self.bot = vk_api.VkApi(token=comunity_token)
        self.api = VkTools(acces_token)
        self.params = None

    def message_send(self, user_id, message, attachment=None):
        self.bot.method('messages.send',
                        {'user_id': user_id,
                         'random_id': get_random_id(),
                         'attachment': attachment,
                         })

    def handler(self):
        longpull = VkLongPoll(self.bot)

        for event in longpull.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message = event.text.lower()
                context = ''
                if message == 'привет':
                    self.params = self.api.get_profile_info(event.user_id)
                    self.message_send(event.user_id, f'привет {self.params["name"]}')

                    if params['bpdate'] == None:
                        context += str(age)
                    if params['city'] == None:
                        context += str(city)
                    if context == 'age':
                        self.message_send(event.user_id, f'У вас не достаточно информации на странице, напишите пожалуйста возраст, например: 40')
                    if context == 'city':
                        self.message_send(event.user_id, f'У вас не достаточно информации на странице, напишите пожалуйста город, например: Москва')
                    if context == 'agecity':
                        self.message_send(event.user_id, f'У вас не достаточно информации на странице, напишите пожалуйста возраст и город через пробел, например: 40 Москва')
                elif context == 'age':
                    params[age] = message
                    del(context)
                elif context == 'city':
                    params[city] = message
                    del(context)
                elif context == 'agecity':
                    age_city = message.split(' ')[0]
                    if age_city.isdigit() == True:
                        params[age] = age_city
                    else:
                        params[city] = age_city
                    age_city_params = message.split(' ')[1]
                    if age_city_params.isdigit() == True:
                        params[age] = age_city_params
                    else:
                        params[city] = age_city_params
                    del(context)
                elif message == 'поиск':
                    self.message_send(event.user_id, f'Начинаем поиск')

                    found_questionnaries = questionnaries()
                        # проверка базы данных
                    saved_profiles = check_user()
                    while saved_profiles == True:
                        found_questionnaries

                    photos_user = self.api.get_photos(user['id'])

                    attachment = ''
                    for num, photo in enumerate(photos_user):
                        attachment += f'photo{photo["owner_id"]}_{photo["id"]}'
                        if num == 2:
                            break
                    self.message_send(event.user_id, f'Встречайте {user["name"]} ссылка:vk.com/{user["id"]}', attachment=attachment)
                    # запись в базу данных
                    add_user()
                elif message == 'пока':
                    self.message_send(event.user_id, f'всего доброго')
                else:
                    self.message_send(event.user_id, f'неизвестная команда')
