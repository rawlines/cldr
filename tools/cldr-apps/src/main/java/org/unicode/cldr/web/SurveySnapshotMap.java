package org.unicode.cldr.web;

import java.util.TreeMap;

public class SurveySnapshotMap implements SurveySnapshot {

    final private TreeMap<String, String> snapMap = new TreeMap<>();

    @Override
    public void put(String snapshotId, String json) {
        snapMap.put(snapshotId, json);
    }

    @Override
    public String get(String snapshotId) {
        return snapMap.get(snapshotId);
    }

    @Override
    public String[] list() {
        Object[] a = snapMap.entrySet().toArray();
        String keys[] = new String[a.length];
        return snapMap.keySet().toArray(keys);
    }
}