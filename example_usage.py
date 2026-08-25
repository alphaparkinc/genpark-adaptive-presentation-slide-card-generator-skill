from client import AdaptivePresentationSlideCardGeneratorClient

def main():
    client = AdaptivePresentationSlideCardGeneratorClient()
    res = client.generate_interactive_deck_cards('Series B Pitch Deck: GenPark Autonomous Developer Ecosystem', 10)
    print('Deck ID: ' + res['deck_card_id'] + ' | ' + res['topic'])
    print('Cards: ' + str(res['slide_cards_generated_count']) + ' cards | Interactive Charts: ' + str(res['embedded_interactive_charts_count']))
    print('Web URL: ' + res['one_click_web_deck_url'] + ' | PPTX Export: ' + str(res['pptx_export_bundle_ready']))

if __name__ == '__main__':
    main()
