  
'''
using discord.py version 1.0.0a
'''
import discord
import asyncio
import re
import multiprocessing
import threading
import concurrent

BOT_OWNER_ROLE = 'RUNNER' # change to what you need
#BOT_OWNER_ROLE_ID = "658721047729668116"
  
 

 
oot_channel_id_list = ["612941582487912458"
"612941582487912458", #loco
"612941822838177793", #confetti
"616711171122135073", #hq
"616710870143205382", #swag iq
"593990608914219008", #Galaxy loco
"593990638916075520", #Galaxy con
"607613349491900436", #iq loco
"590583414541910018", #iq con
"595635734904307742", #TF loco
"605443517069656084", #TF con
"513818250652680213", #trivia world hq
"525131707410677761", #TRIVIA tribe hq
"523359669280833536", #TGL hq
"595639586726740049", #TF hq
"568617830258442255", #revolution
"595639769904447502", #TF swag iq
"535675285211971584", #Trivia world swag
"446448437119025154", #Trivia tribe swag
"585618493093969923", #TGL SWAG
"569420128794443776", #unt Loco
"588070986554015764", #unt Confetti India
"611940220350234686", #UNT flipkart
"569420198717816852", #UNT hq
"627397062794936321", #Trivia hacks
"638670943174131713", #loco 
"638797808735879168", #Jeetho
"638797767627636766", #Hq
"638797953833893894", #Swagiq
"640877280960184332",
"641656808129167371",
"600497255774158848",
"609711581168926720",
"623158370576236559",
"623177013410136064",
"623177221468848135",
"631667692281004032" "640877280960184332",
"641656808129167371",
"600497255774158848",
"609711581168926720",
"623158370576236559",
"623177013410136064",
"623177221468848135",
"631667692281004032"
"631763703049748481"                       

]


answer_pattern = re.compile(r'(not|n)?([1-3]{1})(\?)?(cnf)?(\?)?$', re.IGNORECASE)

apgscore = 500
nomarkscore = 300
markscore = 200

async def update_scores(content, answer_scores):
    global answer_pattern

    m = answer_pattern.match(content)
    if m is None:
        return False

    ind = int(m[2])-1

    if m[1] is None:
        if m[3] is None:
            if m[4] is None:
                answer_scores[ind] += nomarkscore
            else: # apg
                if m[5] is None:
                    answer_scores[ind] += apgscore
                else:
                    answer_scores[ind] += markscore

        else: # 1? ...
            answer_scores[ind] += markscore

    else: # contains not or n
        if m[3] is None:
            answer_scores[ind] -= nomarkscore
        else:
            answer_scores[ind] -= markscore

    return True

class SelfBot(discord.Client):

    def __init__(self, update_event, answer_scores):
        super().__init__()
        global oot_channel_id_list
        #global wrong
        self.oot_channel_id_list = oot_channel_id_list
        self.update_event = update_event
        self.answer_scores = answer_scores

    async def on_ready(self):
        print("======================")
        print("🎭Trivia Hacks||Official🎭")
        print("Connected to discord.")
        print("User: " + self.user.name)
        print("ID: " + str(self.user.id))

    # @bot.event
    # async def on_message(message):
    #    if message.content.startswith('-debug'):
    #         await message.channel.send('d')

        def is_scores_updated(message):
            if message.guild == None or \
                str(message.channel.id) not in self.oot_channel_id_list:
                return False

            content = message.content.replace(' ', '').replace("'", "")
            m = answer_pattern.match(content)
            if m is None:
                return False

            ind = int(m[2])-1

            if m[1] is None:
                if m[3] is None:
                    if m[4] is None:
                        self.answer_scores[ind] += nomarkscore
                    else: # apg
                        if m[5] is None:
                            self.answer_scores[ind] += apgscore
                        else:
                            self.answer_scores[ind] += markscore

                else: # 1? ...
                    self.answer_scores[ind] += markscore

            else: # contains not or n
                if m[3] is None:
                    self.answer_scores[ind] -= nomarkscore
                else:
                    self.answer_scores[ind] -= markscore

            return True

        while True:
            await self.wait_for('message', check=is_scores_updated)
            self.update_event.set()

class Bot(discord.Client):

    def __init__(self, answer_scores):
        super().__init__()
        self.bot_channel_id_list = []
        self.embed_msg = None
        self.embed_channel_id = None
        #global wrong
        self.answer_scores = answer_scores

        # embed creation
        self.embed=discord.Embed(title="ALL ANSWER BOT", description="**Dark Web Searching** :spy:")
        self.embed.set_author(name ='',url=' ',icon_url='https://cdn.discordapp.com/attachments/621954596402888724/629761044717240350/giphy.gif')        
        self.embed.add_field(name="Answer 1", value="~~0.0~~", inline=False)
        self.embed.add_field(name="Answer 2", value="~~0.0~~", inline=False)
        self.embed.add_field(name="Answer 3", value="~~0.0~~", inline=False)
        self.embed.set_image(url="https://cdn.discordapp.com/attachments/621954596402888724/632300887574052884/source-1.gif")
        self.embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/621954596402888724/632299326059839508/GIF-191012_005925.gif")
        self.embed.set_footer(text=f"Made With❤By𝐻𝐴𝐶𝐾𝐸𝑅 𝓡𝓘𝓣𝓔𝓢𝓗 #1645", \
            icon_url="https://cdn.discordapp.com/attachments/621954596402888724/629760302736736296/JPEG_20190609_075619.jpg")
        self.embed.add_field(name="Google Answer:", value="0", inline=True)

        #await self.bot.add_reaction(embed,':spy:')


    async def clear_results(self):
        for i in range(len(self.answer_scores)):
            self.answer_scores[i]=0

    async def update_embeds(self):
      #  global wrong

         

        one_check = ""
        two_check = ""
        three_check = ""
        best_answer = ' :hourglass: '
        

        lst_scores = list(self.answer_scores)
        

        highest = max(lst_scores)
        best_answer = ' :hourglass: '
        lowest = min(lst_scores)
        answer = lst_scores.index(highest)+1
        #global wrong             

        if highest > 0:
            if answer == 1: 
                one_check = ":one:"
                best_answer = ':one:'
            else:
                one_check = "<:x:600303220417626120>"

            if answer == 2:
                two_check = ":two:"
                best_answer = ':two:'
            else:
                two_check = "<:x:600303220417626120>"

            if answer == 3:
                three_check = ":three:"
                best_answer = ':three:'
            else:
                three_check = "<:x:600303220417626120>"

            

        #if lowest < 0:
            #if answer == 1:
                #one_cross = ":x:"
            #if answer == 2:
                #two_cross = ":x:"
            #if answer == 3:
                #three_cross = ":x:"            
 
        self.embed.set_field_at(0, name="Answer 1", value="**{0}**{1}".format(lst_scores[0], one_check))
        self.embed.set_field_at(1, name="Answer 2", value="**{0}**{1}".format(lst_scores[1], two_check))
        self.embed.set_field_at(2, name="Answer 3", value="**{0}**{1}".format(lst_scores[2], three_check))
        self.embed.set_field_at(3, name="Google Answer!:", value=best_answer, inline=True)


        if self.embed_msg is not None:
            await self.embed_msg.edit(embed=self.embed)

    async def on_ready(self):
        print("==============")
        print("🎭Trivia Hacks||Official🎭")
        print("Connected to discord.")
        print("User: " + self.user.name)
        print("ID: " + str(self.user.id))

        await self.clear_results()
        await self.update_embeds()
        #await self.change_presence(activity=discord.Game(name='with '+str(len(set(self.get_all_members())))+' users'))
        await self.change_presence(activity=discord.Activity(type=1,name='BHI BHI KA PYAR||*help'))

    async def on_message(self, message):

        # if message is private
        if message.author == self.user or message.guild == None:
            return

        if message.content.lower() == "+":
            await message.delete()
            if BOT_OWNER_ROLE in [role.name for role in message.author.roles]:
                self.embed_msg = None
                await self.clear_results()
                await self.update_embeds()
                self.embed_msg = \
                    await message.channel.send('',embed=self.embed)
                #await self.embed_msg.add_reaction("✔️")
                self.embed_channel_id = message.channel.id
            else:
                await message.channel.send("**Fuck🖕** You Do Not Have permission To Use This **cmd!** :stuck_out_tongue_winking_eye:")
            return

        if message.content.startswith('*help'):
          await message.delete()
          if BOT_OWNER_ROLE in [role.name for role in message.author.roles]:
           embed = discord.Embed(title="**__HELP COMMANDS__**", description="**__HOW RUN BOT__**", color=0x00ff00)
           embed.add_field(name="**__SUPPORT GAME__** ", value="**Loco\nSwag-iq\nConfett-India\nHQ Trivia**", inline=False)
           embed.add_field(name="**__WHEN QUESTION COME PUT COMMAND__**", value="+   **__is COMMAND WORK FOR ALL SUPPORT GAME__**", inline=False)
           await message.channel.send(embed=embed)
          

        # process votes
        if message.channel.id == self.embed_channel_id:
            content = message.content.replace(' ', '').replace("'", "")
            updated = await update_scores(content, self.answer_scores)
            if updated:
                await self.update_embeds()

def bot_with_cyclic_update_process(update_event, answer_scores):

    def cyclic_update(bot, update_event):
        f = asyncio.run_coroutine_threadsafe(bot.update_embeds(), bot.loop)
        while True:
            update_event.wait()
            update_event.clear()
            f.cancel()
            f = asyncio.run_coroutine_threadsafe(bot.update_embeds(), bot.loop)
            #res = f.result()

    bot = Bot(answer_scores)

    upd_thread = threading.Thread(target=cyclic_update, args=(bot, update_event))
    upd_thread.start()

    loop = asyncio.get_event_loop()
    loop.create_task(bot.start('Njc2MjY1MzM1NzMyODMwMjE4.XkDLUg._etM1VPIBcosu_SAVfDSVksBclQ'))
    loop.run_forever()


def selfbot_process(update_event, answer_scores):

    selfbot = SelfBot(update_event, answer_scores)

    loop = asyncio.get_event_loop()
    loop.create_task(selfbot.start('NjU4NzIxMDQ3NzI5NjY4MTE2.Xj-Qjg.u70Q_My2t4-66RSixv4Bbqrpj8E',
                                   bot=False))
    loop.run_forever()

if __name__ == '__main__':

    # running bot and selfbot in separate OS processes

    # shared event for embed update
    update_event = multiprocessing.Event()

    # shared array with answer results
    answer_scores = multiprocessing.Array(typecode_or_type='i', size_or_initializer=3)

    p_bot = multiprocessing.Process(target=bot_with_cyclic_update_process, args=(update_event, answer_scores))
    p_selfbot = multiprocessing.Process(target=selfbot_process, args=(update_event, answer_scores))

    p_bot.start()
    p_selfbot.start()

    p_bot.join()
    p_selfbot.join()




 
 
