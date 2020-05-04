
import re
def main_regex_matcher(path_test):
    master_list=[]
    sent_list=[]
    data = open(path_test,'r')
    for text in data:
        found = 0
        small_master_list=[]
        sent_list.append(text)
    
        m = re.search(' to (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tommorow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) and ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) as ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thanks (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Remind ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) next ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) when ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' TO (.+?) ON ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 2 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 11 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' on (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) remind ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' will (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) so ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' That (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) will ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' fr (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' should (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomo ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' m (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 3 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' To (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abt (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 2 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' m (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' will (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) I ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' is (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) liquid ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remember (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' dmello (.+?) Tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Pls (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' now (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' To (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 6 (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' we (.+?) varsha ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Whom ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 9pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' really (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) By ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) everyday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Actually (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) as ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' only (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) during ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) Today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Your (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' if (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I (.+?) asked ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' your (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remind (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Good (.+?) Afternoon ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) an ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' club7pm (.+?) also ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' remember (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' For (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) sunday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' And (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' actually (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Plz (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) are ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) so ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Hey (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abt (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 4 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) tonight ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 1 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pause (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' kar (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 35am (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Wednesday (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' About (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tomorrow (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' but (.+?) I ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7am ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 8 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Monday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Arijit ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 4pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' add (.+?) aT ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' at (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) now ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' monday (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) a ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' have (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' also (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' My (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) when ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' everyday (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 9 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) immediately ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' too (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' wen (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 12222 (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Remind (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Kindly (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminde (.+?) due ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tomorow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 4 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) could ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) 7 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Leena (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Good (.+?) morning ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' three (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' TASK (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' that (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 2 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Re (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) notification ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' For (.+?) On ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) top ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) so ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) So ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' want (.+?) to ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) ofter ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) office ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) How ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 5 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 13 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 1 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) 15 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) of ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' when (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 2 (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) ON ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) till ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Actually (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Also (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 30 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' ve (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' will (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 11am ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) and ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tdy ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 7pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) IN ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 18that (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) n ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Even (.+?) If ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tommow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Plea (.+?) e ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' pm (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' year (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' And (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) only ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) aftr ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' schedule (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' months (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' regarding (.+?) officer ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) as ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) movon ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) 11 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) 5 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) within ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' I (.+?) forget ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 17 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) Now ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' November (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' okay (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) 5 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) tom ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' has (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' a (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) mor ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' send (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) due ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Wanna (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' on (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) wed ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 24th (.+?) go ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) are ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' be (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' above (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' and (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' all (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) one ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) around ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' add (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) list ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 2017 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) time ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' is (.+?) Please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) till ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 4000 (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) at10 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) By ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' would (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) will ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' schedule (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Sunday (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' saturday (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' abo (.+?) t ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Schedule ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' want (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) plz ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) after ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' time (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' in (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' please (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) 1 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' as (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) through ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' some (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' reminder (.+?) On ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tho (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) 5pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) time ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 5pm (.+?) instead ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 8pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' it (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' y (.+?) 6pm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' took (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 12 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' i (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 56pm (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Is (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) too ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) 4 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 4PM ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' thank (.+?) you ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) between ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Okay (.+?) 2 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Can (.+?) you ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Thanks (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' need (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) yaa ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) volume ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Will (.+?) this ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Schedule (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Subject (.+?) nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 1pm (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' the (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' cancell (.+?) 5 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' u (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' about (.+?) daily ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) that ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' been (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) 3 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' ll (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) At ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 1o (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Also (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' take (.+?) tomorrow ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' daily (.+?) a ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' ll (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Tcs (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) for ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' About (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Wat (.+?) will ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) by ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) mnday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' urgent (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) toady ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' of (.+?) 31st ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) 45 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Reminder (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 1st (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 2nd (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' am (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 00 (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' in (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' an (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) 6 ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' buy (.+?) please ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Nov ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Some (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' set (.+?) reminder ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) until ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' CSE (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) before ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) called ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) Thursday ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Please (.+?) today ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Dec (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) form ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' me (.+?) due ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' list (.+?) me ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) tom ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' Actually (.+?) is ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' had (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' schedule (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' for (.+?) ymca ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tor (.+?) on ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' 13th (.+?) remind ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' to (.+?) bill ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' you (.+?) every ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' U (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' be (.+?) from ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' A (.+?) days ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' What (.+?) type ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' What (.+?) do ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' want (.+?) in ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' know (.+?) go ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' my (.+?) alarm ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
        m = re.search(' tms (.+?) at ', text)
        if m:
            found = m.group(1)
            small_master_list.append(found)
