import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am a weather bot. Use /weather <city>')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        import requests
        city = " ".join(context.args) if context.args else "Delhi"
        # OpenWeatherMap API example (अपना API key डालें)
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            await update.message.reply_text(f'Weather in {city}: {desc}, {temp}°C')
        else:
            await update.message.reply_text(f'City {city} not found.')
    except ImportError:
        await update.message.reply_text('Requests module not installed.')

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not set")
        return
    
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))
    
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()