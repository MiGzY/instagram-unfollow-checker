#!/usr/bin/env python3
import json
import csv
import argparse

def load_usernames(path, key_guess=None):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict):
        keys = [key_guess, 'relationships_following', 'relationships_followers', 'followers', 'following', 'data', 'relationships', 'users', 'accounts']
        for k in keys:
            if k and k in data and isinstance(data[k], list):
                data = data[k]
                break
        else:
            for v in data.values():
                if isinstance(v, list):
                    data = v
                    break
    if not data:
        return []
    if isinstance(data, list) and data and isinstance(data[0], str):
        return [s.strip() for s in data if s]
    out = []
    for item in data:
        if isinstance(item, str):
            out.append(item.strip())
        elif isinstance(item, dict):
            if 'string_list_data' in item:
                sld = item['string_list_data']
                val = None
                if isinstance(sld, list) and sld and isinstance(sld[0], dict):
                    val = sld[0].get('value')
                if not val:
                    val = item.get('title')
                if val:
                    out.append(str(val).strip())
                    continue
            keys = [key_guess, 'username', 'user', 'handle', 'screen_name', 'name', 'id']
            for k in keys:
                if k and k in item and item[k]:
                    out.append(str(item[k]).strip())
                    break
    return out

def main():
    parser = argparse.ArgumentParser(description="Find Instagram users you follow who don't follow you back.")
    parser.add_argument('--following', required=True, help='Path to following JSON file')
    parser.add_argument('--followers', required=True, help='Path to followers JSON file')
    parser.add_argument('--out', default='not_following_back.csv', help='Output CSV filename')
    parser.add_argument('--lower', action='store_true', help='Case-insensitive comparison')
    parser.add_argument('--key', default=None, help='Key hint for JSON object')
    args = parser.parse_args()

    following = load_usernames(args.following, key_guess=args.key)
    followers = load_usernames(args.followers, key_guess=args.key)

    if args.lower:
        followers_set = {u.lower() for u in followers}
        not_following_back = [u for u in following if u.lower() not in followers_set]
    else:
        followers_set = set(followers)
        not_following_back = [u for u in following if u not in followers_set]

    not_following_back.sort()

    with open(args.out, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'instagram_url'])
        for u in not_following_back:
            writer.writerow([u, f'https://www.instagram.com/{u}'])

    print(f'Following: {len(following)}')
    print(f'Followers: {len(followers)}')
    print(f'Not following back: {len(not_following_back)}')
    print(f'Saved to: {args.out}')

if __name__ == '__main__':
    main()