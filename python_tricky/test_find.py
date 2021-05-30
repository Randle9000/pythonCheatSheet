log = """00> time get_timeESending GET_TIME to Cloud
00> $ [418064581] <info> tr_store: msg:rsv, idx:0, rsvd:1
00> [418064581] <info> tr_store: new tr, src_frmt:DevID ID:0xA00050ABA2, dst_frmt:CldID ID:0x23, tr_idx:0
00> [418064581] <info> tr_store: tr from:stack, c_cls:0x0000, c_id:0x108(rd)
00> [418064582] <info> tr_store: msg:del, idx:0, rsvd:0
00> [418064582] <info> app: Sent time req [1] to CldID over spi.
00> [418065047] <info> app: Parce flex
00> [418065047] <info> tr_store: msg:rsv, idx:0, rsvd:1
00> [418065047] <info> tr_store: new tr, src_frmt:CldID ID:0x20, dst_frmt:DevID ID:0xA00050ABA2, tr_idx:0
00> [418065047] <info> tr_store: tr from:spi, c_cls:0x0000, c_id:0x108(rsp)
00> [418065047] <info> app: Process stack cmd c_cls:0x0000, c_id: 0x0423, data_len: 0x000D
00> [418065047] <info> app: total_drift[0 secs] rt_delay[0 secs] curr_drift[0 secs]
00> [418065047] <info> app: CMD CLASS:0x0000 ID:0x0423 (RP) SUCCESS; STATUS: 0x0"""

pattern = 'CMD CLASS:0x0000'
pattern2 = 'ccc'
print(log.find(pattern))
print(log.find(pattern2))
